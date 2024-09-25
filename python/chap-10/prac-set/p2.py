class Calculator:
    def __init__(self,number):
        self.number = number;

    def getSquare(self):
        return self.number * self.number

    def getCube(self):
        return self.number * self.number * self.number
    def getSqRoot(self):
        return (self.number) ** 1/2 # double * means '1/2' is a exponent/power of (self.number)
    
Num = Calculator(4)
print(Num.getSquare())
print(Num.getCube())
print(Num.getSqRoot())