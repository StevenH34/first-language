"""
Will store all the data of the variables via a dictionary.
"""
class Data:
    def __init__(self) -> None:
        self.variables = {}
    
    def read(self, id):
        return self.variables[id]
    
    def readAll(self):
        return self.variables
    
    def write(self, variable, expression):
        variableName = variable.value
        self.variables[variableName] = expression