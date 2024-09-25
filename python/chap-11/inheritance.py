# It is one of OOP principle, which is use to inherit attribute,method of parent/base class into child class.

# types of inheritance:
# 1- single inheritance 
# 2- multiple inheritance 
# 3- multi-level inheritance 

# single inheritance -> its mean kay jo child class hai wo srf ek single parent ko inherit kregi. like:
class School: # -> parent class or base class
    schoolName = 'St.Paul' 
    location = 'saddar' 

    def showSchoolInfo(self):
        return f' name = {self.schoolName}\n location = {self.location}'
    

class Student(School): # -> child class or derived class
    def __init__(self, name, age):
        self.name = name;
        self.age = age;

    def stdInfo(self):
        return f' name = {self.name}\n age = {self.age}'
    

std1 = Student('shah',12)
print(std1.showSchoolInfo()) # now we can use both method, the method from 'School' class as well from 'Student' class. acha yaha par ek issue ayega wo yeh kay jo showSchoolInfo() hai its a School class method likin isme jo 'name' attribute hai wohi same 'name' attribute 'Student' mabi hai toh iss lia jo School class ka 'name' attribute hai wo override hojayega therefore humna School ka 'name' attribute change krkay 'schoolName' 
print(std1.stdInfo()) 

