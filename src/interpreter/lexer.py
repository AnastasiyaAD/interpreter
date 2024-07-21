import os
import sys

PROJECT_ROOT = os.path.abspath( # to prevent a Python module dependency conflict
    os.path.join(
        os.path.dirname(__file__), 
        os.pardir
    )+'/interpreter'
)
sys.path.append(PROJECT_ROOT)

from token_m import Token
from constant import ConstantsManagement
# Create an instance of ConstantsManagement
constants = ConstantsManagement()
class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]
        self.lex = []

    def move_to_next_pos(self):
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def return_pos(self, pos):
        self.pos = pos
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.move_to_next_pos()
     
    def get_next_token(self): # create a new token from current_char and add it to the token list
        while self.current_char is not None:
            
            if self.current_char.isspace(): # skipping extra spaces
                self.skip_whitespace()
                continue

            if self.current_char == '+':    # PLUS
                self.move_to_next_pos()
                self.lex.append(Token(constants.PLUS, '+'))
                return Token(constants.PLUS, '+')
            
            if self.current_char == '.':    # DOT
                self.move_to_next_pos()
                self.lex.append(Token(constants.DOT, '.'))
                return Token(constants.DOT, '.')

            if self.current_char == '-':    # MINUS
                self.move_to_next_pos()
                self.lex.append(Token(constants.MINUS, '-'))
                return Token(constants.MINUS, '-')

            if self.current_char == '*':    # MULTIPLY
                self.move_to_next_pos()
                self.lex.append(Token(constants.MULTIPLY, '*'))
                return Token(constants.MULTIPLY, '*')

            if self.current_char == '/':    # DIVIDE
                self.move_to_next_pos()
                self.lex.append(Token(constants.DIVIDE, '/'))
                return Token(constants.DIVIDE, '/')

            if self.current_char == '(':    # LPAREN
                self.move_to_next_pos()
                self.lex.append(Token(constants.LPAREN, '('))
                return Token(constants.LPAREN, '(')
            
            if self.current_char == ')':    # RPAREN
                self.move_to_next_pos()
                self.lex.append(Token(constants.RPAREN, ')') )
                return Token(constants.RPAREN, ')') 

            if self.current_char == ']':    # RBRACKET
                self.move_to_next_pos()
                self.lex.append(Token(constants.RBRACKET, ']') )
                return Token(constants.RBRACKET, ']') 

            if self.current_char == '[':    # LBRACKET
                self.move_to_next_pos()
                self.lex.append(Token(constants.LBRACKET, '['))
                return Token(constants.LBRACKET, '[')      

            if self.current_char == ',':    # COMMA
                self.move_to_next_pos()
                self.lex.append(Token(constants.COMMA, ','))
                return Token(constants.COMMA, ',')
            
            if self.current_char == '<':    # LESS and ELESS
                if(self.text[self.pos +1]=='='):
                    self.move_to_next_pos()
                    self.move_to_next_pos()
                    self.lex.append(Token(constants.ELESS, '<='))
                    return Token(constants.ELESS, '<=')
                else:
                    self.move_to_next_pos()
                    self.lex.append(Token(constants.LESS, '<'))
                    return Token(constants.LESS, '<')

            if self.current_char == '>':    # GREATER and EGREATER
                if(self.text[self.pos +1]=='='):
                    self.move_to_next_pos()
                    self.move_to_next_pos()
                    self.lex.append(Token(constants.EGREATER, '>='))
                    return Token(constants.EGREATER, '>=')
                else:
                    self.move_to_next_pos()
                    self.lex.append(Token(constants.GREATER, '>'))
                    return Token(constants.GREATER, '>')

            if self.current_char == '!':    # FALSE
                self.move_to_next_pos()
                self.move_to_next_pos()
                self.lex.append(Token(constants.FALSE, '!='))
                return Token(constants.FALSE, '!=')

            if self.current_char == ';':    # SEMICOLON
                self.move_to_next_pos()
                self.lex.append(Token(constants.SEMICOLON, ';'))
                return Token(constants.SEMICOLON, ';')
            
            if self.current_char == '=':    # ASSIGN and EQUALS
                if(self.text[self.pos +1]=='='):
                    self.move_to_next_pos()
                    self.move_to_next_pos()
                    self.lex.append(Token(constants.EQUALS, '=='))
                    return Token(constants.EQUALS, '==')
                else:
                    self.move_to_next_pos()
                    self.lex.append(Token(constants.ASSIGN, '='))
                    return Token(constants.ASSIGN, '=')
            
            if self.current_char == ':':    # COLON
                self.move_to_next_pos()
                self.lex.append(Token(constants.COLON, ':'))
                return Token(constants.COLON, ':')
            
            if self.current_char == '"':    # STRING
                self.move_to_next_pos()
                token_value = ""
                while self.current_char is not None and self.current_char != '"': 
                    token_value += self.current_char
                    self.move_to_next_pos()
                self.move_to_next_pos()
                self.lex.append(Token(constants.STRING, token_value))
                return Token(constants.STRING, token_value)

            if self.current_char.isdigit(): # NUMBER
                token_value = ""
                while self.current_char is not None and self.current_char not in constants.OPERATIONS: 
                    if self.current_char.isspace(): # removing extra spaces
                        self.skip_whitespace()
                        continue
                    token_value += self.current_char
                    self.move_to_next_pos()

                self.lex.append(Token(constants.NUMBER, int(token_value)))
                return Token(constants.NUMBER, int(token_value))
             
            if self.current_char.isalpha(): # INPUT, PRINT, LAMBDA, IF, ELSE and VARIABLE
                token_value = ""
                while self.current_char is not None and self.current_char not in constants.OPERATIONS and not self.current_char.isspace(): 
                    token_value += self.current_char
                    self.move_to_next_pos()

                if token_value == "print":
                    self.lex.append(Token(constants.PRINT, token_value))
                    return Token(constants.PRINT, token_value)
                elif token_value == "input":
                    self.lex.append(Token(constants.INPUT, token_value))
                    return Token(constants.INPUT, token_value)
                elif token_value == "lambda":
                    self.lex.append(Token(constants.LAMBDA, token_value))
                    return Token(constants.LAMBDA, token_value)
                elif token_value == "if":
                    self.lex.append(Token(constants.IF, token_value))
                    return Token(constants.IF, token_value)
                elif token_value == "end_if":
                    self.lex.append(Token(constants.ENDIF, token_value))
                    return Token(constants.ENDIF, token_value)
                else:
                    self.lex.append(Token(constants.VARIABLE, token_value))
                    return Token(constants.VARIABLE, token_value)
                
            print(f"Incorrect syntax: {self.text}")
            sys.exit()

        self.lex.append(Token(constants.END, None)) # code line ending pointer
        return Token(constants.END, None)    

    def get_tokens (self): # return the token list
        while self.current_char is not None:
            self.get_next_token()
        return self.lex     