# self paramter


class Employee:
    language = "python"
    salary = 500000
    # defining method in class

    def getInfo():
        print(
            f"he work on {language} and get {salary}"
        )  # here raising error bcuz its not proper way to access any attribute.


sharoon = Employee()
# print(sharoon.getInfo())
# now yaha par ek error ayega that is "Employee.getInfo() takes 0 positional arguments but 1 was given"

# likin humna toh koi argumnet pass hi nhi kia toh yeh kiu keh raha hai 1 argument was given.

# so uski waja yeh haka behind the scene by default jab be hum kisi class say koi instance create krtay hain toh usme jo methods hotay hain unko jo instance/object create krtay hain as a argument pass hota hai.so basicaly behind the scene yeh iss tarah call hota hai:

# Employee.getInfo(
#     sharoon
# )  # toh ab zahir agr koi argument pass ho rha hai toh jo function body bnai hai usme koi parameter be toh hona jo usse get kray so isi lia hum usme ek parameter create kreinga.

# above is error and its explanation.


class Person:
    language = "Js"
    salary = 100000

    def getInfo(
        self,
    ):  # yeh zarori nhi haka parameter name 'self' hi ho, its just a convention.
        print(
            f"he work on {self.language} and get {self.salary}"
        )  # now we will not get error bcuz we have learned in above example that it is neccessary to set parameter while defining method.


shah = Person()
shah.getInfo()  # now we will not get error.
Person.getInfo(shah)
 # access .getInfo() from above line way and this way both is same.

# -----------------------
# @staticmethod (decorator) -> yeh decorator hum tab use kreinga jab jasa koi class bnai humnay or usme hum koi asa method bnaya jo ka koi be dynamic value nhi access kr rha toh jab wo koi dynamic value be access nhi kr rha toh hr hum chahay gay kay usme jo 'self' parameter hum pass krtay hain wo be na krein bcuz we dont want to access anything,toh for that purpose we will use '@staticmethod'.


class Company:
    location = "PAK"
    category = "software"

    @staticmethod
    def getName():
        print('Company name is Techverse51')


Company1= Company()
Company1.getName()