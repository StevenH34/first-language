"""
Post-order traversal: Left subtree -> Right subtree -> Root Node
"""
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
            return leftValue + rightValue
        elif operator.value == "-":
            return leftValue - rightValue

    def interpret(self):
        leftNode = self.tree[0]     # Left subtree
        rightNode = self.tree[2]    # Right subtree
        operator = self.tree[1]     # Root node
        
        return self.computeBinary(leftNode, operator, rightNode)