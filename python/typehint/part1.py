from typing import List, Dict, Set
# https://docs.python.org/3/library/typing.html

# Now remember type hinting in python is introduced after 3.5 version.

# and basically jo built-in type hint in python ayein hain, wo srf humay reading may helpout krtay hain kay like temp1: str = 'shah' . or ab agar 'temp1' variable ko number value dengay toh phr be error nhi ayega show hoga kay you are using wrong types. So if we want that kay humay development time pa hi error show hon so then we will use 'mypy' for that purpose. 

# e.g 1
# x: str = 1 # Now why its not giving error ? so jasa kay mena uper be btya hai kay yeh jo isme typehinting hogi wo srf bta rhi haka its better to assign 'string' value to this variable but it is not forcing that this variable should be 'string'. Therefore it will not raise any error on the development time or runtime as well. 

# Now if we want to make it static and strongly typing so we have to use an additional module named as 'MYPY'.
# step1 -> pip install mypy
# step2 -> go in terminal and run 'mypy' at your project directory and write "mypy fileName "
# now everytime if you want to check type error in your file so you have run your file using 'mypy'.

# variable annotation
X: int = 2 # now here mypy will not raise error bcuz type and value are compatible. 
y = "str"  
# y= 8 # but here you encounter error bcuz first we have assigned string value to 'y' and then on the next line we are assigning integer value.

# function annotation
def sum(n1:int, n2:int, n3) -> int :
    return n1 + n2 + n3

print(sum(1,2,3))

# def mul(n1:int, n2:int, n3:int) -> int : # error bcuz function is returning integer but we have not returning it. therefore we can use 'None' if func is not returning.
#      print(n1 * n2 * n3)

# mul(2,3,4)

# list annotation
l1:list[str] =['a','b','c']

# l2:list[str] =['a','b','c',4] # error bcuz we use int value in list of string.

l3:list[list[int]] = [[1,2],[3,4],[5,6]] # Now when we create nested list or 2d array, so it will raise error bcuz 'list[list[int]]' this is not valid way to make 2d list. so to prevent it you have to import 'List' from typing module then write it like this: 'List[list[int]]'.

l4: List[list[str]] = [['a','b'],['c','d']] 

# Dictionary annotation
d1:dict[str,str] = {'name':'shah'}
# another way to do dictionary annotation is importing 'Dict' object from typing module.
d2: Dict[int,str] = {0 : 'sharoon'}
# d2: Dict[int,str] = {'0' : 'sharoon'} # error

# Set annotation
s1: set[bool] = {True,False}
# another way
s2 : Set[float] = {1.2,3.6,2}



