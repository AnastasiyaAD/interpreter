import sys
class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def define(self, var_name, value):
        self.symbols[var_name] = value

    def is_included(self, var_name, value): # returns true if it is in the symbol_table 
        if var_name in self.symbols:
                if self.symbols[var_name] == value:
                    return True
        return False

    def get_var(self, var_name):
        if var_name in self.symbols:
            return self.symbols[var_name]
        print(f"The variable {var_name} is not defined")
        sys.exit()
        
    def get_value(self, value): # returns the variable with value = input if it is in the symbol_table 
        for var_name in self.symbols:
            if self.symbols[var_name] == value:
                return var_name
        print(f"The value {value} is not defined")
        sys.exit()

