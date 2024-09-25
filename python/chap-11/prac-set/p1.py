class TwoDVector:
    def __init__(self,i,j):
        self.i = i; 
        self.j = j; 

    def show(self):
        return f'the vector is {self.i}i + {self.j}j'

class ThreeDVector(TwoDVector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k; 

    def show(self):
        return f'the vector is {self.i}i + {self}j + {self.k}k'
    

twoD1 = TwoDVector(1,3); 
print(twoD1.show())# yaha par jo show() method 'TwoDVector' ma hai wo invoke hojayega.
threeD1 = ThreeDVector(1,3,5); 
print(threeD1.show()) # but yeh class nay toh TwoDVector ko inherit kia hai ab usme be show() hai and isme be show() toh konsa wala show method execute hoga toh basic jo 'ThreeDVector' ka show() hai wo run hojayega bcuz wo usko override krdega and this is also known as 'polymorphism' 