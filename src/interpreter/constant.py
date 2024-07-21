from enum import Enum

# token types Constants
class TokenTypeConstants:
    NUMBER = "NUMBER" # int
    STRING = "STRING" # "Hello World !"
    VARIABLE = 'VARIABLE' # x 

    PLUS = "PLUS"
    MINUS = "MINUS"
    ASSIGN = "ASSIGN" # =
    MULTIPLY = "MULTIPLY"
    DIVIDE = "DIVIDE"

    COMMA = "COMMA" # ,
    LPAREN = "LPAREN" # (
    RPAREN = "RPAREN" # )
    LBRACKET = "LBRACKET" # [
    RBRACKET = "RBRACKET" # ]
    SEMICOLON = "SEMICOLON" # ;
    QUOTES = "QUOTES" # "
    COLON = "COLON" # :
    DOT = "DOT" # .

    PRINT = "PRINT"
    INPUT = "INPUT"
    END = "END" # code line ending pointer P.S. the user doesn't use this
    LAMBDA = "LAMBDA" 
    # input add_two = lambda x, y : x + y; 
    # add_two(2,3);
    # 5

    IF = "IF"
    ENDIF = "ENDIF"
    LESS = "LESS" # <
    GREATER = "GREATER" # >
    EQUALS = "EQUALS" # ==
    ELESS = "ELESS" # <=
    EGREATER = "EGREATER" # >=
    FALSE = "FALSE" # !=

    OPERATIONS = ['=','+','-','*','/','(',')',';',',','[',']', '"',':', '>', '<', '!', '.']

    

# ConstantsManagement class
class ConstantsManagement:
    def __init__(self):
        # Set constants from separate classes as attributes
        for cls in [TokenTypeConstants]:
            for key, value in cls.__dict__.items():
                if not key.startswith("__"):
                    self.__dict__.update(**{key: value})

    def __setattr__(self, name, value):
        raise TypeError("Constants are immutable")

