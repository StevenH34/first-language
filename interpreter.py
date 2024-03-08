"""
Post-order traversal: Left subtree -> Right subtree -> Root Node
"""
from tokens import Integer, Float

class Interpreter:
    def __init__(self, tree, base):
        self.tree = tree
        self.base = base

    def read_INT(self, value):
        return int(value)

    def read_FLT(self, value):
        return float(value)

    def read_VAR(self, id):
        variable = self.base.read(id)
        variableType = variable.type
        return getattr(self, f"read_{variableType}")(variable.value)

    def computeBinary(self, leftNode, operator, rightNode):
        leftType = "VAR" if str(leftNode.type).startswith("VAR") else str(leftNode.type)
        rightType = "VAR" if str(rightNode.type).startswith("VAR") else str(rightNode.type)

        if operator.value == "=":
            leftNode.type = f"VAR({rightType})"
            self.base.write(leftNode, rightNode)
            return self.base.readAll()
        
        leftValue = getattr(self, f"read_{leftType}")(leftNode.value)
        rightValue = getattr(self, f"read_{rightType}")(rightNode.value)
        
        match operator.value:
            case "+":
                result = leftValue + rightValue
            case "-":
                result = leftValue - rightValue
            case "*":
                result = leftValue * rightValue
            case "/":
                result = leftValue / rightValue
            case ">":
                result = 1 if leftValue > rightValue else 0
            case ">=":
                result = 1 if leftValue >= rightValue else 0
            case "<":
                result = 1 if leftValue < rightValue else 0
            case "<=":
                result = 1 if leftValue <= rightValue else 0
            case "==":
                result = 1 if leftValue == rightValue else 0
            case "and":
                result = 1 if leftValue and rightValue else 0
            case "or":
                result = 1 if leftValue or rightValue else 0

        return Integer(result) if (leftType == "INT" and rightType == "INT") else Float(result)
    
    def computeUnary(self, operator, operand):
        operandType = "VAR" if str(operand.type).startswith("VAR") else str(operand.type)
        operand = getattr(self, f"read_{operandType}")(operand.value)
        
        if operator.value == "+": 
            return +operand
        elif operator.value == "-":
            return -operand
        elif operator.value == "not":
            return 1 if not operand else 0

    def interpret(self, tree=None):
        if tree is None: tree = self.tree
        
        # Unary operation
        if isinstance(tree, list) and len(tree) == 2:
            expression = tree[1]
            if isinstance(expression, list):
                expression = self.interpret(expression)
            return self.computeUnary(tree[0], expression)
        elif not isinstance(tree, list):
            return tree
        else:
            leftNode = tree[0]     # Left subtree
            if isinstance(leftNode, list):
                leftNode = self.interpret(leftNode)

            rightNode = tree[2]    # Right subtree
            if isinstance(rightNode, list):
                rightNode = self.interpret(rightNode)
            
            operator = tree[1]     # Root node            
            return self.computeBinary(leftNode, operator, rightNode)