# __main__.py
import os
from lexer import Lexer
from parser import Parser
from symbol_table import SymbolTable
def main():
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_path = "data.txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    f = open(abs_file_path)
    x = f.readlines()
    f.close()
    text_input = ""
    for i in range (0,len(x)):
        text_input+=x[i]

    print(f"{text_input} \n")
    lexer = Lexer(text_input)
    symbol_table = SymbolTable()
    lambda_table = SymbolTable()
    parser = Parser(lexer,symbol_table,lambda_table)
    parser.parse()

if __name__ == "__main__":
    main()