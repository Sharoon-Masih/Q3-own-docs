# ---------multiple-inheritance--------
# the senerio in which the child class inherit more than one parent class, so that type of inheritance is known as multiple inheritance.

class Car:
    modal = "corolla"; 
    company = "toyota"; 
    
    def showCarInfo(self):
        return f'modal = {self.modal}\n company = {self.company}'
    
class Bike:
    modal = "R1"; 
    company = "yamaha"; 
    
    def showBikeInfo(self):
        return f'modal = {self.modal}\n company = {self.company}'

class Person(Car,Bike): # -> ab yaha par yeh jo Person class hna isne 'Car' and 'Bike' dono class ko inherit kia hai and it is called multiple inheritance.
    def __init__(self, name, age):
        self.name = name; 
        self.age = age; 
    def showPersonInfo(self):
        return f' name = {self.name}\n age = {self.age}'
    
person1 = Person('shah',30)
print(person1.showCarInfo()) # yaha par be yeh msla aa rha hai kay jo Car class hai usme be 'modal' and 'company' hain and Bike mabi due to that jo Car ma modal and company attribute hai they are taking preference again BIke class attribute bcuz the 1st parameter class attribute has more preference.
print(person1.showBikeInfo())