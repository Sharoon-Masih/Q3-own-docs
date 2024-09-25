

def func(): # ab basically function may jitnay variable declare krtay hain toh unka scope function scope hota hai mtlb kay wo srf function ka andar accessible hotay hain out of function nhi. 
    a = 5; 
    print(a); 

func(); 
# print(a); # like here you can see that 'a' cannot be accessible outside of function.

# now basically 'global' keyword ka through hum ek global variable create krka usko within function be use krsktay hain and out of function be use krsktay hain.

b = 40; 

def show():
    b = 3; 
    print(b); # here 'b' is local variable of function 'show'.

print(b); # ab yaha jo 'b' variable print hoga wo jo uper create kia hai wo hoga.  
show(); # or yaha jo 'b' print hoga wo show() function wala hoga.

# now ab agr hum global keyword ka use krka jo variable hum out of function use kreinga wo inside the function use kreinga.

c = 35; 
def showC():
    global c; 
    print(c); 

print(c) # ab yaha jo 'c' uper declare kia hai wohi print hoga.
showC(); # or isme be jo 'c' print hoga wo wohi hoga jo uper declare kiya.