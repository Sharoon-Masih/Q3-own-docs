class Vector:
    def __init__(self,x,y,z):
        self.x = x; 
        self.y = y; 
        self.z = z;

    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y,self.z+self.z)
    
    def __mul__(self,other):
        return Vector(self.x*other.x, self.y*other.y,self.z*other.z)
    
    def __str__(self):
        return f'Vector({self.x},{self.y},{self.x})'
    
v1 = Vector(2,5,7); 
v2 = Vector(3,4,7); 
print(v1 + v2); 
print(v1 * v2); 