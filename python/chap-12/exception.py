# Exception Handling in python:
# There are many built-in exceptions in python which ar e raised when any thing wrong happen.
# exception in python can be handled usig a 'try' statement.
# the code that handle exception/error is written in except clause. its like try/catch block in JS/TS.

# try:
#     # code that may raise an exception
# except Exception as e:
#     print(e) # if any error so here it will be printed otherwise the try block will execute.

# x=5/0; # like its a zeroDivision error which means that we cannot divide by zero.But ab msla yeh haka jasa hi yeh program run hoga toh code ka flow ruk jayega mtlb kay error hojayega, now to solve this porblem we use exception handling.
# print('continue..')

try:
    x = 5/0; 
except Exception as e:
    print(e) # ZeroDivisionError: division by zero simply error print hojayega but code flow will be continue.so it prevents your program from crashing.
print('continue...')

# e.g 2
a = int(input('enter num: ')) # it will raise error when i will string instead of integer, so now how to handle it. bcuz jo user hi wo toh kuch be krskta hai and its our responsibility to handle it. so iska liya hum try..except block use krsktay hain.
print(a) 

try:
    a = int(input('enter num: ')) # it will raise error when i will enter string.
    print(a)
except Exception as e:
    print(e)

# --------------
# ab hum specific error ko be handle krsktay hain or general error ko be.

try:
    a = int(input('enter num: ')) #pehla toh main code yeh hai jo execute hoga then iskay resu;t ki base pa yeh faisla hoga kay agr toh koi be error nhi hua toh nicha wala koi be block execute nhi hoga otherwise agr error hoga toh jo nicha 2 specific except block define kiya hain agr unme say koi error hoga toh wo execute hojayega otherwise jo general except block hai which is 'Exception' block usmay get hojyega error.
    print(a)  
except ValueError as v: # for handling specific 'ValueError'
    print('value error')
    print(v)
except ZeroDivisionError as z: # for handling specific 'ZeroDivisionError'
    print('zeroDivision error')
    print(z)
except Exception as e: # for getting any error .
    print(e)

# Now is difference b/w just except block and except block with Exception class.
try:
    a = int(input('enter your phone: ')) 
except: # ab jo srf except block ka bd humna code kia hna usmay srf 'invalid input' likha ayega but yeh nhi pta chlega kayy yeh error kya hai bcuz wo humna get hi nhi hor rha.
# toh in short if you want exact error msg so use Exception, if you want to only print static msg you can direct write it in except block. 
    print('invalid input')

# ---------------------------------------
