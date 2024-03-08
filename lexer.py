"""
"5 + 3" [5, +, 3], "7.2  * 4" [7.2, *, 4]
Take care of ints, floats, & ignore spaces
Need to add vars, if statements, while loops
"""
from tokens import Operation, Integer, Float, Declaration, Variable, Boolean, Comparison

class Lexer:
    digits = "0123456789"
    letters = "abcdefghijklmnopqrstuvwxyz"
    operations = "+-/*()="
    stopwords = [" "]
    declarations = ["make"]
    boolean = ["and", "or", "not"]
    comparison = ["<", "<=", ">", ">=", "=="]
    specialCharacters = "<>="

    def __init__(self, text):
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
                nextChar = self.text[self.index+1]
                if nextChar != "=":
                    self.token = Operation(self.char)
                    self.move()
                else:
                    self.detectSpecialCharacters()
            elif self.char in Lexer.stopwords:
                self.move()
                continue
            elif self.char in Lexer.letters:
                word = self.extractWord()
                if word in Lexer.declarations:
                    self.token = Declaration(word)
                elif word in Lexer.boolean:
                    self.token = Boolean(word)
                else:
                    self.token = Variable(word)
            elif self.char in Lexer.specialCharacters:
                self.detectSpecialCharacters()

            self.tokens.append(self.token)
        return self.tokens

    def detectSpecialCharacters(self):
        comparisonOperator = ""
        while self.char in Lexer.specialCharacters and self.index < len(self.text):
            comparisonOperator += self.char
            self.move()
        self.token = Comparison(comparisonOperator)

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
