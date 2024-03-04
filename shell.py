from lexer import Lexer

while True:
    text = input("Input: ")
    tokenizer = Lexer(text)
    tokens = tokenizer.tokenize()
    print(tokens)