# Conditional exp 
# for single condtion we can use 'if' clause
# for multiple conditions we can use 'if-elif-else' clause, basic in python 'elif' is serving a role of 'else if'.

# syntax 
# single if condition

a = 20; 
if(a > 10):
    print('a is greater')

# if-else condition
if(a <= 5): 
    print('a is less than 5'); 
else:
    print('a is greater than 5')


# if-elif-else condition (it is used for taking multiple decision, also known as if-elif-else ladder)
if(a == 10):
    print('a is 10'); 
elif( a > 10):
    print('a is greater than 10'); 
elif(a < 8):
    print('a is less than 8'); 
else:
    print('a is 8 or greater than 8')

# Now here is something important that in python indentation does matter, In other languages we use curly braces to define the scope but in python y doing indentation its scope is defined

marks = 80
# if marks >= 80:
# print(" Grade A+ ") # now you will get error bcuz humna indentation nhi ki properly jo usko asa lg rha haka yaha print statement is out of 'if' scope.
# --------------------------
gradeDict = {
    100:"A+",
    90:"A+",
    80:"A",
    70:"B",
    60:"C",
}
if marks >=80:
    aliMrks = 80
    print("Grade A with: ",aliMrks)
elif marks < 80:
    aliMrks = marks
    print(f"Grade {gradeDict[aliMrks]} with: ",aliMrks)
else:
    print("Invalid Marks") 

# ----------------------------------------
#  yaha par multiple statement ki ek trick smjhay gay.
temp = 20; 
if temp%2 < 20:
    print("true"); 
if temp > 20:  # ab basic yaha par yeh confusion hoti haka ek pehla 'if' statement hai phr usme nichay ek or 'if' statement hai toh wo kesay posible hai toh basically wo jo uper if statement hai wo seperate hai nichay wali say which means wo single if statement hai 
    print("temp is > 20"); 
elif temp >=15:
    print("temp is >= 15"); 
else: 
    print("invalid") 

# --------------------------
# The pass Statement
# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
a = 33
b = 200

if b > a:
  pass

# --------------------------
# 'in' keyword
names = ['shahabuddin','yasir','abeera','faryal']
inputName = input('Enter your name: ')
if inputName in names: # basic yeh jo 'in' ka keyword hna iskay through hum one line ma check krsktay hain kya jo input value ayi hai wo 'names' exist krti hai ya nhi.
    print('you can login')
else:
    print('you cannot login')

# e.g 2
str = 'hello how are you ?'
if 'hello' in str: # 'in' keyword can check in string also.
    print('hello found'); 
