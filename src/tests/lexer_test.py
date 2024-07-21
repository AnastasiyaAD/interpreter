import unittest
import os
import sys

PROJECT_ROOT = os.path.abspath( # to prevent a Python module dependency conflict
    os.path.join(
        os.path.dirname(__file__), 
        os.pardir
    )
)
sys.path.append(PROJECT_ROOT)

from interpreter.constant import ConstantsManagement
from interpreter.lexer import Lexer

# Create an instance of ConstantsManagement
constants = ConstantsManagement()

class TestLexerCase(unittest.TestCase):

    def test_space(self):
        text_input = 'print ( 4 +4 - 2)   ;'
        l = Lexer(text_input)
        tokens = l.get_tokens()
        self.assertEqual(tokens[0].value, "print")
        self.assertEqual(tokens[1].value, "(")
        self.assertEqual(tokens[2].value, 4)
        self.assertEqual(tokens[2].type, constants.NUMBER)
        self.assertEqual(tokens[3].value, "+")
        self.assertEqual(tokens[4].value, 4)
        self.assertEqual(tokens[4].type, constants.NUMBER)
        self.assertEqual(tokens[5].value, "-")
        self.assertEqual(tokens[6].value, 2)
        self.assertEqual(tokens[6].type, constants.NUMBER)
        self.assertEqual(tokens[7].value, ")")
        self.assertEqual(tokens[8].value, ";")

    def test_string(self):
        text_input = 'print( "xrt" +"r")   ;'
        l = Lexer(text_input)
        tokens = l.get_tokens()
        self.assertEqual(tokens[0].value, "print")
        self.assertEqual(tokens[1].value, "(")
        self.assertEqual(tokens[2].value, 'xrt')
        self.assertEqual(tokens[2].type, constants.STRING)
        self.assertEqual(tokens[3].value, "+")
        self.assertEqual(tokens[4].value, 'r')
        self.assertEqual(tokens[4].type, constants.STRING)
        self.assertEqual(tokens[5].value, ")")
        self.assertEqual(tokens[6].value, ";")
    
    def test_list(self): # test list of string, list of digital and input variable
        text_input = 'input x = ["cccc","dddd", " ssss"], y=[2,3 , 5 ];'
        l = Lexer(text_input)
        tokens = l.get_tokens()
        self.assertEqual(tokens[0].value, "input")
        self.assertEqual(tokens[1].value, "x")
        self.assertEqual(tokens[1].type, constants.VARIABLE)
        self.assertEqual(tokens[2].value, "=")
        self.assertEqual(tokens[3].value, "[")
        self.assertEqual(tokens[4].value, 'cccc')
        self.assertEqual(tokens[4].type, constants.STRING)
        self.assertEqual(tokens[5].value, ",")
        self.assertEqual(tokens[6].value, 'dddd')
        self.assertEqual(tokens[7].value, ",")
        self.assertEqual(tokens[8].value, ' ssss')
        self.assertEqual(tokens[9].value, "]")
        self.assertEqual(tokens[10].value, ",")
        self.assertEqual(tokens[11].value, "y")
        self.assertEqual(tokens[11].type, constants.VARIABLE)
        self.assertEqual(tokens[12].value, "=")
        self.assertEqual(tokens[13].value, "[")
        self.assertEqual(tokens[14].value, 2)
        self.assertEqual(tokens[14].type, constants.NUMBER)
        self.assertEqual(tokens[15].value, ",")
        self.assertEqual(tokens[16].value, 3)
        self.assertEqual(tokens[16].type, constants.NUMBER)
        self.assertEqual(tokens[17].value, ",")
        self.assertEqual(tokens[18].value, 5)
        self.assertEqual(tokens[18].type, constants.NUMBER)
        self.assertEqual(tokens[19].value, "]")
        self.assertEqual(tokens[20].value, ";")

    def test_lambda(self):
        text_input = 'input add_two = lambda x, y : x + y;'
        l = Lexer(text_input)
        tokens = l.get_tokens()
        self.assertEqual(tokens[0].value, "input")
        self.assertEqual(tokens[0].type, constants.INPUT)

        self.assertEqual(tokens[1].value, "add_two")
        self.assertEqual(tokens[1].type, constants.VARIABLE)

        self.assertEqual(tokens[2].value, "=")
        self.assertEqual(tokens[2].type, constants.ASSIGN)

        self.assertEqual(tokens[3].value, "lambda")
        self.assertEqual(tokens[3].type, constants.LAMBDA)

        self.assertEqual(tokens[4].value, "x")
        self.assertEqual(tokens[4].type, constants.VARIABLE)

        self.assertEqual(tokens[5].value, ",")
        self.assertEqual(tokens[5].type, constants.COMMA)

        self.assertEqual(tokens[6].value, "y")
        self.assertEqual(tokens[6].type, constants.VARIABLE)

        self.assertEqual(tokens[7].value, ":")
        self.assertEqual(tokens[7].type, constants.COLON)

        self.assertEqual(tokens[8].value, "x")
        self.assertEqual(tokens[8].type, constants.VARIABLE)

        self.assertEqual(tokens[9].value, "+")
        self.assertEqual(tokens[9].type, constants.PLUS)

        self.assertEqual(tokens[10].value, "y")
        self.assertEqual(tokens[10].type, constants.VARIABLE)

        self.assertEqual(tokens[11].value, ";")
        self.assertEqual(tokens[11].type, constants.SEMICOLON)

    def test_comparison(self): # > < >= <= == !=
        text_input = 'x > y; x<y; x>=y; x<=y; x==y; x!=y;'
        l = Lexer(text_input)
        tokens = l.get_tokens()
        self.assertEqual(tokens[0].value, "x")
        self.assertEqual(tokens[0].type, constants.VARIABLE)

        self.assertEqual(tokens[1].value, ">")
        self.assertEqual(tokens[1].type, constants.GREATER)

        self.assertEqual(tokens[2].value, "y")
        self.assertEqual(tokens[2].type, constants.VARIABLE)

        self.assertEqual(tokens[3].value, ";")
        self.assertEqual(tokens[3].type, constants.SEMICOLON)

        self.assertEqual(tokens[4].value, "x")
        self.assertEqual(tokens[4].type, constants.VARIABLE)

        self.assertEqual(tokens[5].value, "<")
        self.assertEqual(tokens[5].type, constants.LESS)

        self.assertEqual(tokens[6].value, "y")
        self.assertEqual(tokens[6].type, constants.VARIABLE)

        self.assertEqual(tokens[7].value, ";")
        self.assertEqual(tokens[7].type, constants.SEMICOLON)

        self.assertEqual(tokens[8].value, "x")
        self.assertEqual(tokens[8].type, constants.VARIABLE)

        self.assertEqual(tokens[9].value, ">=")
        self.assertEqual(tokens[9].type, constants.EGREATER)
        
        self.assertEqual(tokens[10].value, "y")
        self.assertEqual(tokens[10].type, constants.VARIABLE)

        self.assertEqual(tokens[11].value, ";")
        self.assertEqual(tokens[11].type, constants.SEMICOLON)

        self.assertEqual(tokens[12].value, "x")
        self.assertEqual(tokens[12].type, constants.VARIABLE)

        self.assertEqual(tokens[13].value, "<=")
        self.assertEqual(tokens[13].type, constants.ELESS)

        self.assertEqual(tokens[14].value, "y")
        self.assertEqual(tokens[14].type, constants.VARIABLE)

        self.assertEqual(tokens[15].value, ";")
        self.assertEqual(tokens[15].type, constants.SEMICOLON)

        self.assertEqual(tokens[16].value, "x")
        self.assertEqual(tokens[16].type, constants.VARIABLE)

        self.assertEqual(tokens[17].value, "==")
        self.assertEqual(tokens[17].type, constants.EQUALS)

        self.assertEqual(tokens[18].value, "y")
        self.assertEqual(tokens[18].type, constants.VARIABLE)

        self.assertEqual(tokens[19].value, ";")
        self.assertEqual(tokens[19].type, constants.SEMICOLON)

        self.assertEqual(tokens[20].value, "x")
        self.assertEqual(tokens[20].type, constants.VARIABLE)

        self.assertEqual(tokens[21].value, "!=")
        self.assertEqual(tokens[21].type, constants.FALSE)

        self.assertEqual(tokens[22].value, "y")
        self.assertEqual(tokens[22].type, constants.VARIABLE)

        self.assertEqual(tokens[23].value, ";")
        self.assertEqual(tokens[23].type, constants.SEMICOLON)

    def test_cond(self): # if 
        text_input = '''if (x > 3):
                            x = 2;
                            print("yes");
                        end_if'''
        
        l = Lexer(text_input)
        tokens = l.get_tokens()

        self.assertEqual(tokens[0].value, "if")
        self.assertEqual(tokens[0].type, constants.IF)

        self.assertEqual(tokens[1].value, "(")
        self.assertEqual(tokens[1].type, constants.LPAREN)

        self.assertEqual(tokens[2].value, "x")
        self.assertEqual(tokens[2].type, constants.VARIABLE)

        self.assertEqual(tokens[3].value, ">")
        self.assertEqual(tokens[3].type, constants.GREATER)

        self.assertEqual(tokens[4].value, 3)
        self.assertEqual(tokens[4].type, constants.NUMBER)

        self.assertEqual(tokens[5].value, ")")
        self.assertEqual(tokens[5].type, constants.RPAREN)

        self.assertEqual(tokens[6].value, ":")
        self.assertEqual(tokens[6].type, constants.COLON)

        self.assertEqual(tokens[7].value, "x")
        self.assertEqual(tokens[7].type, constants.VARIABLE)

        self.assertEqual(tokens[8].value, "=")
        self.assertEqual(tokens[8].type, constants.ASSIGN)

        self.assertEqual(tokens[9].value, 2)
        self.assertEqual(tokens[9].type, constants.NUMBER)

        self.assertEqual(tokens[10].value, ";")
        self.assertEqual(tokens[10].type, constants.SEMICOLON)

        self.assertEqual(tokens[11].value, "print")
        self.assertEqual(tokens[11].type, constants.PRINT)

        self.assertEqual(tokens[12].value, "(")
        self.assertEqual(tokens[12].type, constants.LPAREN)

        self.assertEqual(tokens[13].value, "yes")
        self.assertEqual(tokens[13].type, constants.STRING)

        self.assertEqual(tokens[14].value, ")")
        self.assertEqual(tokens[14].type, constants.RPAREN)

        self.assertEqual(tokens[15].value, ";")
        self.assertEqual(tokens[15].type, constants.SEMICOLON)

        self.assertEqual(tokens[16].value, "end_if")
        self.assertEqual(tokens[16].type, constants.ENDIF)