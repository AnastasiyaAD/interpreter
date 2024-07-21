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

from interpreter.lexer import Lexer
from interpreter.parser import Parser
from interpreter.symbol_table import SymbolTable

class TestParserCase(unittest.TestCase):
    def test_expr(self):
        text_input = 'print ( 4 +4 - 2)   ;'
        lexer = Lexer(text_input)
        symbol_table = SymbolTable()
        lambda_table = SymbolTable()
        parser = Parser(lexer,symbol_table,lambda_table)
        parser.parse()
        self.assertEqual(parser.output, 6)

    def test_term(self):
        text_input = 'print ( 4 *4 / 2)   ;'
        lexer = Lexer(text_input)
        symbol_table = SymbolTable()
        lambda_table = SymbolTable()
        parser = Parser(lexer,symbol_table,lambda_table)
        parser.parse()
        self.assertEqual(parser.output, 8)

    def test_expr_str(self):
        text_input = 'print ( "d" + "r")   ;'
        lexer = Lexer(text_input)
        symbol_table = SymbolTable()
        lambda_table = SymbolTable()
        parser = Parser(lexer,symbol_table,lambda_table)
        parser.parse()
        self.assertEqual(parser.output, "dr")

    def test_term_str(self):
        text_input = 'print ( "d" * 3 )   ;'
        lexer = Lexer(text_input)
        symbol_table = SymbolTable()
        lambda_table = SymbolTable()
        parser = Parser(lexer,symbol_table,lambda_table)
        parser.parse()
        self.assertEqual(parser.output, "ddd")
        
    def test_input(self):
        text_input = 'input  x = 4, y = "ddddd", z = [ 1, 4], k = [" a", "b", "c"] ;'
        lexer = Lexer(text_input)
        symbol_table = SymbolTable()
        lambda_table = SymbolTable()
        parser = Parser(lexer,symbol_table,lambda_table)
        parser.parse()
        self.assertTrue(parser.symbol_table.is_included('x',4))
        self.assertTrue(parser.symbol_table.is_included('y',"ddddd"))
        self.assertTrue(parser.symbol_table.is_included('z',[ 1, 4]))
        self.assertTrue(parser.symbol_table.is_included('k',[" a", "b", "c"]))

    def test_cond(self):
        text_input = '''if (4 > 3):
                            print("yes");
                        end_if'''
        lexer = Lexer(text_input)
        symbol_table = SymbolTable()
        lambda_table = SymbolTable()
        parser = Parser(lexer,symbol_table,lambda_table)
        parser.parse()
        self.assertEqual(parser.output, "yes")
    
    def test_cond_var(self):
        text_input = '''input x = 4, y = 8;
                        if (x > 3):
                            x = 2 * y;
                        end_if
                        if (x > 3):
                            y = y + 2 * x;
                        end_if
                        print(x,y);'''
        lexer = Lexer(text_input)
        symbol_table = SymbolTable()
        lambda_table = SymbolTable()
        parser = Parser(lexer,symbol_table,lambda_table)
        parser.parse()
        self.assertEqual(parser.output, [16, 40])
    
    def test_lambda(self):
        text_input = '''input summa = lambda x, y : print(x + y);.
                        value = summa(2,3);
                        print(value);  '''
        lexer = Lexer(text_input)
        symbol_table = SymbolTable()
        lambda_table = SymbolTable()
        parser = Parser(lexer,symbol_table,lambda_table)
        parser.parse()
        self.assertTrue(parser.symbol_table.is_included('summa',('x', 'y')))
        self.assertTrue(parser.lambda_table.get_var(('x', 'y')))
        self.assertEqual(parser.output,5)

    def test_lambda_cond(self):
        text_input = '''input max = lambda a, b : print( if (a > b): print(a); end_if if (a < b): print(b); end_if;);.
                        value = max(6,9);
                        print(value);  '''
        lexer = Lexer(text_input)
        symbol_table = SymbolTable()
        lambda_table = SymbolTable()
        parser = Parser(lexer,symbol_table,lambda_table)
        parser.parse()
        self.assertEqual(parser.output,9)