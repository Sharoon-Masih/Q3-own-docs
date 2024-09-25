class Animals:
    a1 = 'lion'; 
    a2 = 'tiger'; 
    a3 = 'dog'; 
    a4 = 'cat'; 
    a5 = 'cow'; 
    a6 = 'rhino'; 

class Pets(Animals):
    p1 = 'cat'; 
    p2 = 'dog'; 
    p3 = 'rabbit'; 
    p4 = 'cow'; 

class Dog(Pets):
    
    @staticmethod
    def bark():
        return 'Woof! woof!'