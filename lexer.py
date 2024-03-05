"""
"5 + 3" [5, +, 3], "7.2  * 4" [7.2, *, 4]
Take care of ints, floats, & ignore spaces
Need to add vars, if statements, while loops
"""
from tokens import Operation, Integer, Float, Declaration, Variable

class Lexer:
    digits = "0123456789"
    letters = "abcdefghijklmnopqrstuvwxyz"
    operations = "+-/*()="
    stopwords = [" "]
    declarations = ["make"]

    def __init__(self, text) -> None:
        self.text = text
        self.index = 0
        self.tokens = []
        self.char = self.text[self.index]
        self.token = None
    
    def tokenize(self):
        while self.index < len(self.text):
            if self.char in Lexer.digits:
                self.token = self.extractNumber()
            elif self.char in Lexer.operations:
                self.token = Operation(self.char)
                self.move()
            elif self.char in Lexer.stopwords:
                self.move()
                continue
            elif self.char in Lexer.letters:
                word = self.extractWord()
                if word in Lexer.declarations:
                    self.token = Declaration(word)
                else:
                    self.token = Variable(word)

            self.tokens.append(self.token)
        return self.tokens

    def extractNumber(self):
        number = ""
        isFloat = False
        while (self.char in Lexer.digits or self.char == ".") and (self.index < len(self.text)):
            if self.char == ".":
                isFloat = True
            number += self.char
            self.move()
        return Integer(number) if not isFloat else Float(number)
    
    def extractWord(self):
        word = ""
        while self.char in Lexer.letters and self.index < len(self.text):
            word += self.char
            self.move()
        return word
    
    def move(self):
        self.index += 1
        if self.index < len(self.text):
            self.char = self.text[self.index]
