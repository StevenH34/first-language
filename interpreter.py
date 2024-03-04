"""
Post-order traversal: Left subtree -> Right subtree -> Root Node
"""
from tokens import Integer, Float

class Interpreter:
    def __init__(self, tree):
        self.tree = tree

    def read_INT(self, value):
        return int(value)
    
    def read_FLT(self, value):
        return float(value)

    def computeBinary(self, leftNode, operator, rightNode):
        leftType = leftNode.type
        rightType = rightNode.type

        leftValue = getattr(self, f"read_{leftType}")(leftNode.value)
        rightValue = getattr(self, f"read_{rightType}")(rightNode.value)
        
        if operator.value == "+":
            result = leftValue + rightValue
        elif operator.value == "-":
            result = leftValue - rightValue
        elif operator.value == "*":
            result = leftValue * rightValue
        elif operator.value == "/":
            result = leftValue / rightValue
        
        return Integer(result) if (leftType == "INT" and rightType == "INT") else Float(result)

    def interpret(self, tree=None):
        if tree is None: tree = self.tree

        leftNode = tree[0]     # Left subtree
        if isinstance(leftNode, list):
            leftNode = self.interpret(leftNode)

        rightNode = tree[2]    # Right subtree
        if isinstance(rightNode, list):
            rightNode = self.interpret(rightNode)

        operator = tree[1]     # Root node
        
        return self.computeBinary(leftNode, operator, rightNode)