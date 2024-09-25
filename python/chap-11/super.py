class Employee:
    a = 1
    def __init__(self,name,age,department,salary):
        self.name = name
        self.age = age
        self.department = department
        self.salary = salary

    def showEmpInfo(self):
       return f'{self.name}, {self.age}, {self.department}'

class Coder(Employee): 
    def __init__(self,lang,name,age,department,salary): # Now ab yaha jasay mena Employee ko inherit kia hai Coder class may toh agr ab Employee class ka constructor call krna hai Coder class may toh uskay liya super call krni hogi.
     super().__init__(name=name,age=age,department=department,salary=salary) # ab 'Employee' class kay constructor ko call krkay usmay jo argument require hain wo pass krdiya takay ab jo Employee class may methods ko attribute ki zarorat hai wo access krleinga. 
     self.lang = lang; 

class Programmer(Coder): 
    c = 3


coder1 = Coder('Js','john',25,'software',200000)
print(coder1.showEmpInfo()) 