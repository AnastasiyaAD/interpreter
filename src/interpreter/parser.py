import math
import os
import sys
import re

PROJECT_ROOT = os.path.abspath( # to prevent a Python module dependency conflict
    os.path.join(
        os.path.dirname(__file__), 
        os.pardir
    )+'/interpreter'
)
sys.path.append(PROJECT_ROOT)

from lexer import Lexer
from symbol_table import SymbolTable
from constant import ConstantsManagement
# Create an instance of ConstantsManagement
constants = ConstantsManagement()
class Parser(): #performs the task of syntax checking and code execution (include abstract syntax tree)
    def __init__(self, lexer, symbol_table, lambda_table):
        '''Constructor of the Parser class.

        Parameters:
        - lexer: An instance of the Lexer class for tokenizing the input text.
        - symbol_table: An instance of the SymbolTable class for tracking variables.
        - lambda_table: An instance of the SymbolTable class for tracking lambda.
        symbol_table -  is an object of the SymbolTable class, used to store and manage variables.'''
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()
        self.symbol_table = symbol_table
        self.lambda_table = lambda_table
        self.output = ""

    def eat(self, token_type):
        '''The function checks the current token and the token from which we want to switch to another token.
        That is, we will not be able, being on Token(VAR, "x"), to switch to the next token from the one we pass to the function: 
        Current token: VAR, we passed the PRINT token to the function - we get an error because we are on the VAR token,
        but we want to switch to the next token from the token PRINT.'''
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            raise Exception(f"Error eating {self.current_token.type} token!")
     
    def factor(self):
        """
        The function is responsible for using the built-in language functions that return values
        int 
        variable
        string 
        ()
        """
        token = self.current_token
        if token.type == constants.NUMBER: # int
            self.eat(constants.NUMBER)
            return token.value
        
        elif token.type == constants.VARIABLE: # variable
            self.eat(constants.VARIABLE)
            value = self.symbol_table.get_var(token.value)
            return value
        
        elif token.type == constants.STRING: # string
            string_value = token.value
            self.eat(constants.STRING)
            return string_value
        
        elif token.type == constants.LBRACKET: # list
            self.eat(constants.LBRACKET)
            values = []
            while self.current_token.type != constants.RBRACKET:
                values.append(self.current_token.value)
                self.eat(self.current_token.type)
                if self.current_token.type == constants.COMMA:
                    self.eat(constants.COMMA)
            self.eat(constants.RBRACKET)
            return values
        
        elif token.type == constants.LPAREN:
            self.eat(constants.LPAREN)
            result = self.expr()
            self.eat(constants.RPAREN)
            return result
        
    def term(self):
        """
        Processing of a term (product or quotient).

        Returns:
        - The result of calculating the term.
        """
        result = self.factor()
        while self.current_token.type in (constants.MULTIPLY, constants.DIVIDE):
            token = self.current_token
            if token.type == constants.MULTIPLY:
                self.eat(constants.MULTIPLY)
                result *= self.factor()
            elif token.type == constants.DIVIDE:
                self.eat(constants.DIVIDE)
                result /= self.factor()
        return result
    
    def expr(self):
        """
        Processing of a sum or difference.
        if the lambda is returned, the parser is called for the string of the lambda function

        Returns:
        - The result of calculating
        """
        result = self.term()
        if(isinstance(result, tuple)): # call the parser for the lambda function string
            self.eat(constants.LPAREN)
            func ='input '
            for index, value in enumerate(result): #adding input with variables to the lambda function string 
                func +=str(value)+" "+ "= "+str(self.current_token.value)
                self.eat(self.current_token.type)
                if(self.current_token.type==constants.COMMA):
                    func += ','
                    self.eat(constants.COMMA)
            func +=';'
            self.eat(constants.RPAREN)
            func += self.lambda_table.get_var(result)
            l = Lexer(func)
            s_table = SymbolTable()
            l_table = SymbolTable()
            parser = Parser(l,s_table,l_table)
            parser.parse()
            result = parser.output
        while self.current_token.type in (constants.PLUS, constants.MINUS):
            token = self.current_token
            if token.type == constants.PLUS:
                self.eat(constants.PLUS)
                result += self.term()
            elif token.type == constants.MINUS:
                self.eat(constants.MINUS)
                result -= self.term()
        return result
    
    def cond(self):
        """
        Processing of a comparisons.
        Returns:
        - true or false 
        """
        result = self.term()
        while self.current_token.type in (constants.LESS, constants.GREATER, constants.EQUALS ,constants.ELESS,constants.EGREATER, constants.FALSE): 
            token = self.current_token

            if token.type == constants.LESS:
                self.eat(constants.LESS)
                result = result < self.term()

            elif token.type == constants.ELESS:
                self.eat(constants.ELESS)
                result = result <= self.term()

            elif token.type == constants.GREATER:
                self.eat(constants.GREATER)
                result = result > self.term()

            elif token.type == constants.EGREATER:
                self.eat(constants.EGREATER)
                result = result >= self.term()

            elif token.type == constants.EQUALS:
                self.eat(constants.EQUALS)
                result = result == self.term()
                
            elif token.type == constants.FALSE:
                self.eat(constants.FALSE)
                result = result != self.term()
        return result
    
    def if_type(self): # token processing from IF to ENDIF
        self.eat(constants.IF) 
        self.eat(constants.LPAREN) 
        value = self.cond()
        self.eat(constants.RPAREN)
        self.eat(constants.COLON)
        if(value):
            while self.current_token.type != constants.ENDIF:
                self.statement()
        else:
            while self.current_token.type != constants.ENDIF:
                self.eat(self.current_token.type)
        self.eat(constants.ENDIF)
        
    def statement(self):
        '''The function is responsible for the built-in functions and constructions,
            which do not return values:

          print()
          input = ...
          if ...
          x =

        '''
        if self.current_token.type == constants.PRINT:      # print
            self.eat(constants.PRINT)
            self.eat(constants.LPAREN)
            values = []
            if( self.current_token.type == constants.IF):
                while self.current_token.type != constants.SEMICOLON:
                    self.if_type()
                self.eat(constants.SEMICOLON)
                self.eat(constants.RPAREN)
                self.eat(constants.SEMICOLON)
                print(self.output)
            else:
                while self.current_token.type != constants.END and self.current_token.type != constants.RPAREN:
                    values.append(self.expr())
                    if self.current_token.type == constants.COMMA:
                        self.eat(constants.COMMA)
                self.eat(constants.RPAREN)
                self.eat(constants.SEMICOLON)
                if(len(values)==1):
                    self.output = values[0]
                    print(self.output)
                else:
                    self.output = values
                    print(self.output)

        elif self.current_token.type == constants.VARIABLE: # variable
            var_name = self.current_token.value
            self.eat(constants.VARIABLE)
            self.eat(constants.ASSIGN)
            value = self.expr()
            self.symbol_table.define(var_name, value)
            self.eat(constants.SEMICOLON)

        elif self.current_token.type == constants.INPUT:    # input
            self.eat(constants.INPUT)
            while self.current_token.type != constants.SEMICOLON:             # get all variables with value 
                var_name = self.current_token.value
                if self.current_token.type == constants.VARIABLE:
                    self.eat(constants.VARIABLE)
                    self.eat(constants.ASSIGN)
                    if self.current_token.type == constants.LAMBDA:           # find new lambda func
                        self.eat(constants.LAMBDA)
                        list_variables = ()
                        while self.current_token.type != constants.COLON:     # get lambda tuple of variables 
                            list_variables += (self.current_token.value,)
                            self.eat(self.current_token.type)
                            if self.current_token.type == constants.COMMA:
                                self.eat(constants.COMMA)
                        self.eat(constants.COLON)
                        list_func = ""
                        while self.current_token.type != constants.DOT: # get lambda function string
                            list_func+=self.current_token.value + " "
                            self.eat(self.current_token.type)
                        self.lambda_table.define(list_variables, list_func)   # add new lambda to lambda_table
                        value = list_variables                             
                        self.symbol_table.define(var_name, value)
                        self.eat(constants.DOT)                         # add variable with tuple of lambda variables to symbol_table
                    else:
                        value = self.expr()                                   # add variable to symbol_table
                        self.symbol_table.define(var_name, value)
                        if self.current_token.type == constants.COMMA:
                            self.eat(constants.COMMA)
                
            self.eat(constants.SEMICOLON)

        elif self.current_token.type == constants.IF:       # if
            self.if_type()

        else:
            self.current_token = self.lexer.get_next_token()

    def parse(self):
        while self.current_token.type != constants.END:
            self.statement()

    
