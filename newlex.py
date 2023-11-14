class Lexer:
 def __init__(self, text):
 self.text = text
 self.pos = -1
 self.current_char = None
 self.advance()
 def advance(self):
 self.pos += 1
 self.current_char = self.text[self.pos] if self.pos < len(self.text) else None
 def make_tokens(self):
 print("Tokens are: ")
 modified_ip = ''
 temp = ''
 inc = 0
 while self.current_char != None:
 if self.current_char in ' \t\n':
 self.advance()
 modified_ip += ' '
 elif self.current_char in DIGITS:
 temp = self.current_char
 while self.text[self.pos + 1] in DIGITS:
 self.advance()
 temp += self.current_char
 print(f"Constant : {temp}")
 modified_ip += temp
 self.advance()
 elif self.current_char == '+':
 temp = self.current_char
 if self.text[self.pos + 1] == '+':
 self.advance()
 temp += self.current_char
 print(f"Increment Operator : {temp}")
 modified_ip += temp
 else:
 print(f"Addition Operator : {temp}")
 modified_ip += temp
 self.advance()