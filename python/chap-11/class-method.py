class Employee:
    a = 1; 

    def show(self):
        print(f"printing the class attribute {self.a}")


E1 = Employee()
E1.a = 50; 
E1.show() # Now the value of 'a' which is going to print here is "50" bcuz the instance attribute has more preference than class attribute. but to overcome this issue that if we want kay yaha jo 'a' print ho wo class attribute wala hi ho toh we will use '@classmethod' decorator.

class Student:
    lang = "eng"

    @classmethod 
    def show(cls): # not compulsory to set parameter name as 'cls'.
        print(f"printing the class attribute {cls.lang}")

S1 = Student()
S1.lang = "hindi"
S1.show() # printing the class attribute 'eng'