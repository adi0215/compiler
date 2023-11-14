import re

keywords = ["begin", "end", "auto", "double", "int", "integer", "struct", "break", "else", "printf", "scanf", "to", "Procedure", "or", "and", "long", "switch", "case", "enum", "register", "typedef", "char", "extern", "return", "union", "const", "short", "float", "unsigned", "continue", "for", "signed", "void", "default", "goto", "then", "sizeof", "volatile", "do", "if", "static", "while", "endfor", "endif", "End", "PRINT", "BEGIN", "END", "INTEGER", "REAL", "STRING", "FOR", "TO", "GOTO"]
paranthesis = ["{", "}", "(", ")", "[", "]"]
operators = ["+", "-", "*", "/", ">", "<", "=", "|", "&", "++", "--", ":=", ",", "&&", "||", "!", ">>", "<<", ">=", "<=", "==", "+=", "-=", "*=", "/=", "%=", "^", "~", "sizeof", "?:"]
special_symbols = ["#", ";"]

def handle_numbers(input_str):
    double_regex = r"([+\-]?(?:0|[1-9]\d*)(?:\.\d*)?(?:[eE][+\-]?\d+)?)"
    int_regex = r"(\d+)"
    
    if re.fullmatch(int_regex, input_str):
        i = int(input_str)
        print(input_str, "is an INTEGER")
        return True
    elif re.fullmatch(double_regex, input_str):
        d = float(input_str)
        print(input_str, "is a FLOATING POINT")
        return True
    return False

def handle_input(s):
    if s in operators:
        print(s, "is an Operator")
    elif s in paranthesis:
        print(s, "is a Parenthesis")
    elif s in keywords:
        print(s, "is a Keyword")
    elif s in special_symbols:
        print(s, "is a special symbol")
    else:
        if not handle_numbers(s):
            print(s, "is an Identifier")

if __name__ == "__main__":
    s = ""
    str_occ = ""
    flag = False

    with open("p6.txt", "r") as file:
        for line in file:
            for word in line.split():
                if word[0] == '"' or flag:
                    str_occ = str_occ + " " + word + " "
                    flag = True
                    if word[-1] == '"':
                        print(str_occ, "is a string")
                        str_occ = " "
                        flag = False
                else:
                    handle_input(word)
