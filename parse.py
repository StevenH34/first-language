class Parser:
    def __init__(self, tokens) -> None:
        self.tokens = tokens
        self.index = 0
        self.token = self.tokens[self.index]

    def parse(self):
        return self.expression()

    def factor(self): # Check if INT or FLT
        if self.token.type == "INT" or self.token.type == "FLT": 
            return self.token
    
    def term(self):
        leftNode = self.factor()
        self.move()
        while self.token.value == "*" or self.token.value == "/":
            operation = self.token
            self.move()
            rightNode = self.factor()
            self.move()
            leftNode = [leftNode, operation, rightNode]
        return leftNode
    
    def expression(self):
        leftNode = self.term()
        while self.token.value == "+" or self.token.value == "-":
            operation = self.token
            self.move()
            rightNode = self.term()
            leftNode = [leftNode, operation, rightNode]
        return leftNode


    def move(self):
        self.index += 1
        if self.index < len(self.tokens):
            self.token = self.tokens[self.index]