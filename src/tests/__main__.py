# __main__.py
import unittest
from lexer_test import TestLexerCase
from parser_test import TestParserCase

def lexer_suite(): 
    suite = unittest.TestSuite()
    suite.addTest(TestLexerCase('test_space'))      #  text_input = 'print ( 4 +4 - 2)   ;'
    suite.addTest(TestLexerCase('test_string'))     #  text_input = 'print( "xrt" +"r")   ;'
    suite.addTest(TestLexerCase('test_list'))       #  text_input = 'input x,y; x = ["cccc","dddd", " ssss"]; y=[2,3 , 5 ];'
    suite.addTest(TestLexerCase('test_lambda'))     #  text_input = 'input add_two = lambda x, y : x + y;'
    suite.addTest(TestLexerCase('test_comparison')) #  text_input = 'x > y; x<y; x>=y; x<=y; x==y; x!=y'
    suite.addTest(TestLexerCase('test_cond'))       #  if 
    return suite
 
def parser_suite():
    suite = unittest.TestSuite()
    suite.addTest(TestParserCase('test_expr'))        #  text_input = 'print ( 4 +4 - 2)   ;'
    suite.addTest(TestParserCase('test_term'))        #  text_input = 'print ( 4 *4 / 2)   ;'
    suite.addTest(TestParserCase('test_expr_str'))    #  text_input = 'print ( "d" + "r")   ;'
    suite.addTest(TestParserCase('test_term_str'))    #  text_input = 'print ( "d" * 3 )   ;'
    suite.addTest(TestParserCase('test_input'))       #  text_input = 'input  x = 4, y = "ddddd", z = [ 1, 4], k = [" a", "b", "c"] ;'
    suite.addTest(TestParserCase('test_cond'))        #  if without variable
    suite.addTest(TestParserCase('test_cond_var'))    #  if with variable
    suite.addTest(TestParserCase('test_lambda'))      #  input summa = lambda x, y : print(x + y);
    suite.addTest(TestParserCase('test_lambda_cond')) #  input max = lambda a, b : if (a > b): print(a); end_if if (a < b): print(b); end_if;
    return suite

def main():
    runner = unittest.TextTestRunner()
    print("Lexer:")
    runner.run(lexer_suite())
    print("Parser:")
    runner.run(parser_suite())

if __name__ == "__main__":
    main()