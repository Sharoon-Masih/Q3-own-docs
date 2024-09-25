class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, complexNum):
        # return (self.r + complexNum.r) + (self.i + complexNum.i) # it is also correct way to add but as we know kay real number and imaginary part (iota) add nhi hosktay toh iss lia hum srf yeh chahtay hain jo real part hon both object kay wo apas ma add hojaye and imaginary part apas ma or iss format may string return hojaye. '4 + 6i'

        # 1st way
        #  return f'{self.r + complexNum.r} + {self.i + complexNum.i}i' # ek way yeh haka hum yaha say direct format string hi return krdein but its not proper way.
    
        # 2nd and proper way
        return Complex(self.r+complexNum.r,self.i+complexNum.i) # yeh proper way hai isme basic hum ek Complex class ka hi instance return kr rhay hain jismay jo real part hai wo 1st parameter may add krka put krdia and imaginary part 2nd parameter may.
    
    # ab kiu kay __add__ number value ya string value nhi return krega blka ek 'Complex' object return krega toh usko string ma represent krnay ka liya hum __str__ method ka use kreinga.
    def __str__(self):
        return f'{self.r} + {self.i}i'
    
        
c1 = Complex(1,2); 
c2 = Complex(3,4); 
print(c1 + c2)  