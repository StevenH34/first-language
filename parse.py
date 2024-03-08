class Parser:
    def __init__(self, tokens) -> None:
        self.tokens = tokens
        self.index = 0
        self.token = self.tokens[self.index]

    def parse(self):
        return self.statement()
    
    def variable(self):
        if self.token.type.startswith("VAR"):
            return self.token
        
    def move(self):
        self.index += 1
        if self.index < len(self.tokens):
            self.token = self.tokens[self.index]

    def factor(self): # Check if INT or FLT
        if self.token.type == "INT" or self.token.type == "FLT": 
            return self.token
        elif self.token.value == "(":
            self.move()
            expression = self.booleanExpression()
            return expression
        elif self.token.value == "not":
            operator = self.token
            self.move()
            return [operator, self.booleanExpression()]
        elif self.token.type.startswith("VAR"):
            return self.token
        elif self.token.value == "+" or self.token.value == "-":
            operator = self.token
            self.move()
            operand = self.booleanExpression()
            return [operator, operand]

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
    
    def booleanExpression(self):
        leftNode = self.comparisonExpression()    
        while self.token.type == "BOO":
            operation = self.token
            self.move()
            rightNode = self.comparisonExpression()
            leftNode = [leftNode, operation, rightNode]
        return leftNode
    
    def comparisonExpression(self):
        leftNode = self.expression()    
        while self.token.type == "COM":
            operation = self.token
            self.move()
            rightNode = self.expression()
            leftNode = [leftNode, operation, rightNode]
        return leftNode
    
    def statement(self):
        if self.token.type == "DEC":
            self.move()
            leftNode = self.variable()
            self.move()
            if self.token.value == "=":
                operation = self.token
                self.move()
                rightNode = self.booleanExpression()
                return [leftNode, operation, rightNode]
        elif self.token.type == "INT" or self.token.type == "FLT" or self.token.type == "OPR" or self.token.value == "not":
            return self.booleanExpression()
    