import re

# Define regular expressions for tokens
token_patterns = [
    (r'Procedure', 'PROCEDURE'),
    (r'If', 'IF'),
    (r'if', 'IF'),
    (r'else', 'ELSE'),
    (r'END IF', 'END_IF'),
    (r'elseif', 'ELSE_IF'),
    (r'printf', 'PRINTF'),
    (r':=', 'ASSIGNMENT'),
    (r'=', 'EQUALS'),
    (r'and', 'AND'),
    (r'AND', 'AND'),
    (r'then', 'THEN'),
    (r'integer', 'INTEGER'),
    (r'[a-zA-Z][a-zA-Z0-9]*', 'IDENTIFIER'),
    (r'[0-9]+', 'INTEGER_LITERAL'),
    (r';', 'SEMICOLON'),
    (r':', 'COLON'),
    (r'\(', 'LPAREN'),
    (r'\)', 'RPAREN'),
   (r'".*?"', 'STRING_LITERAL'),
    (r'\s+', None),  
]

# Combine regular expressions into a single pattern
token_pattern = '|'.join(f'({pattern})' for pattern, _ in token_patterns)

# Tokenize the source code
def tokenize(source_code):
    tokens = []
    for match in re.finditer(token_pattern, source_code):
        for i in range(len(token_patterns)):
            pattern, token_type = token_patterns[i]
            if match.group(i + 1):
                if token_type:
                    tokens.append((token_type, match.group(i + 1)))
                break
    return tokens

# Example usage
source_code = """
X: integer ;
Procedure foo( b : integer ) 
b := 13; 
If x = 12 and b = 13 then 
    printf( "by copy-in copy-out" ); 
elseif x = 13 and b = 13 then 
    printf( “by address” );
else 
    printf( "A mystery" );
end if; 
end foo
"""

tokens = tokenize(source_code)
for token in tokens:
    print(token)
