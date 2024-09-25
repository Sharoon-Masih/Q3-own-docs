# multi-level inheritance
# iska mtlb hai kay jasa ek parent class hai 'Employee' ab usko ek child class nay inherit krlia named as 'Coder', ab jo 'Coder' class hai usko ek or child class nay inherit krlia which is 'Programmer'.
# toh basic in above analogy 3 level ban gye 1st level pay - 'EMployee', then 'Coder', then 'Programmer'. so jahan iss type ki inheritance hogi usko multi-level inheritance kahingay.

# e.g

class Employee: # ab remember jo Employee class hai srf jo uska pss ek property hai usko hi access krskti hai which is 'a'
    a = 1


class Coder(Employee): # but yaha jo Coder class hai yeh 'a' and 'b' dono ko access krskti hai.
    b = 2


class Programmer(Coder): # and Programmer class 'a', 'b' and 'c' teeno ko access krskti hai or yehi levels ki waja say isko multi-level inheritance kehtay hain.
    c = 3
