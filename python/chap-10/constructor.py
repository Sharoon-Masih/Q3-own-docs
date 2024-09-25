# like in other languages there is always a constructor function in class, which always invoke when the instance is created from that class(mtlb ka jab be koi instance create hoga uss class say uska jo constructor hai jo ek by default method hai wo automatically invoke hojayega beshak usko hum class may explicitly call kray ya na kray. )

# in python this constructor is named as '__init__()' which automatically invoke when the instance/object is created from that specific class.

# extra: In pythonn the function start with double underscore are known as 'dunder' method  like: __str__ etc.

class Bike:
    company = 'honda'; 
    capacity = '500cc'; 

    def __init__(self): # remember 'self' parameter is compulsory as we have learned about it in  
        
        print('its a bike class instance')


R2 = Bike(); #now you will see that humna __init__ method ko call nhi kia but wo automatically call hojata hai.

# Now if we want to pass instance attribute the class constructor instead of passing like this:
R2.modal = 2012; 
R2.price = 2000000; 
# we can pass like this:
# R3 = Bike(2012,200000) # right now it will rasie error bcuz constructor of Bike class is only accepting one arg which is 'self'

# -----------------------
class Car:
    company = 'toyota'; 
    transmission = 'auto'; 

    def __init__(self,name,modal,price):
        self.name = name; # now yaha jo humna name, modal, price as a argument get kia hain wo self.name, self.modal ko assign kr rhay hain bcuz yeh jo self parameter hna its required in every method which is accessing dynamic value. so basically self.name, self.modal yeh new instance attribute create kr rhay hain jokay dusray methods mabi call krsktay hain. 
        self.modal = modal; 
        self.price = price; 
        print(f'the car name is {self.name} \n modal : {self.modal}\n price : {self.price}')

    def getInfo(carInfo): # so ab jasa uper constructor ma humna new attribute create krdiya ab wo kisi be method may ya direct be access krsktay hain like: Car.name
        print(f'car name is {carInfo.name} and modal is {carInfo.modal}')

Car1= Car('corolla',modal=2015,price=2700000); 
Car1.getInfo(); 
print(Car1.price)

# ----------------------------------------------------

class Mobile:
    company = 'apple'; 
    series = 'iphone'; 

    # wrong way

    # def __init__(name,modal,price,info): # now this will not return the expected result bcuz always remember __init__ may jo 1st parameter hai wo as a self parameter hota hai mtlb kay kay basic jitnay be new attribute create hongay or unko value assign kreinga wo first parameter ka through hi hongay but yaha toh hum last parameter ka through kr rhay hain which is not correct, its mean kay jo first parameter hai uska name zarori nhi kay 'self' hi ho but yeh zarori hai kay jitnay be new attribute set hongay wo uskay through hi hongay. 

    # agar __init__ 1st parameter pa hover be krka check krein toh phr be pta chl jayega

    #     info.name = name; 
    #     info.modal = modal; 
    #     info.price = price; 
    #     print(f'the car name is {info.name} \n modal : {info.modal}\n price : {info.price}')

    # correct way
    def __init__(info,name,modal,price): 
        info.name = name; 
        info.modal = modal; 
        info.price = price; 
        print(f'the mobile name is {info.series+info.name} \n modal : {info.modal}\n price : {info.price}')

myMob = Mobile('X',2020,40000)


# ----------------------------------------------
# The __str__() Function
# The __str__() function controls what should be returned when the class object is represented as a string.

# If the __str__() function is not set, the string representation of the object is returned:

class Person:
    def __init__( self,name,age):
        self.name = name; 
        self.age = age; 

P1 = Person('john',20); 
print(P1) # it will not return the person info like name, age. we can display it by using print statement but it is not the proper way. 

# so the proper way is to create a __str__ func which automatically return the string in the format we set with out calling it:
class Emp:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def __str__(self):
        return f'{self.name}= salary : {self.salary} & age = {self.age}'
    

Emp1 = Emp('pual',20,20000)
print(Emp1)