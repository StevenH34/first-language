
class Token:
    def __init__(self, type, value) -> None:
        self.type = type
        self.value = value
    
    def __repr__(self) -> str:
        return str(self.value)

class Integer(Token):
    def __init__(self, value) -> None:
        super().__init__("INT", value)

class Float(Token):
    def __init__(self, value) -> None:
        super().__init__("FLT", value)

class Operation(Token):
    def __init__(self, value) -> None:
        super().__init__("OPR", value)