from lexer import Lexer
from parse import Parser
from interpreter import Interpreter

while True:
    text = input("Input: ")

    tokenizer = Lexer(text)
    tokens = tokenizer.tokenize()
    
    parser = Parser(tokens)
    tree = parser.parse()

    interpreter = Interpreter(tree)
    print(interpreter.interpret())

