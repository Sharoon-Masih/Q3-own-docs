# A function is a block of code which only runs when it is called.

# You can pass data, known as parameters, into a function.

# A function can return data as a result.


# creating a func
# syntax
def funcName(para1, para2):
    print(para1, para2)
    # func body with indentation if we dont indent it, the statement is not counted to be inside the function.


# calling a func
# funcName() #if func require argument and we dont pass it so it show error at runtime.

funcName("first", "second")


# Parameters or Arguments?
# The terms parameter and argument can be used for the same thing: information that are passed into a function.

# From a function's perspective:

# A parameter is the variable listed inside the parentheses in the function definition.

# An argument is the value that is sent to the function when it is called.


# -----------------------------------
# default argument
def greet(
    name="unknown",
):  # default argument ka faida yeh haka ab argument na be put kreinga toh no problem.
    print("Hello, " + name)


inputName = input("your name: ")
greet(inputName)

# arbitrary argument


def average(
    *num,
):  # just put * with parameter name and also remember jab hum parameter ko arbitrary bnadeta hain toh uski type 'tuple' infer krti hai python which means kay
    avg = (sum(num)) / len(num)
    print("the average of number entered is: ", avg)


average(1, 3, 4, 7, 7)


def selectingArg(*arg):
    print("argument at index 2 = ", arg[2])


selectingArg(1, 2, 3)

# Keyword Arguments
# You can also send arguments with the key = value syntax.


def myFriend(f1, f2, f3):
    print(f1, f2, f3)


myFriend(f1="shah", f2="abdul", f3="rehamn")


# return values
# In python jab hum function create krtay hain toh by default wo return nhi krta value , so uska liya humay explicitly return keyword use krna hai.
def sumNum(*num): #remember agr hum apnay function ka name 'sum' rakhein gay toh error ayega bcuz sum() func is already built-in in python.
    return (sum(num))

print(sumNum())

