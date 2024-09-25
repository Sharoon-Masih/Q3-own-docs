# advance type hinting
from typing import List,Tuple,Union,Dict #ach basically for getting type hint of collection or we can say advance type hint we can use 'typing' module.

# also remember yeh jo behind the scene 'typing' module import ho rha hai wo 'types.py' ki file say ho rha hai isslia jab humari be ek file ka name types.py tha toh its raising error.

l1 : List[int] = [1,2,3,'4']; # remember yebi jo explicitly type set kreinga wo srf intellisense ma help kregi and developer ko guide krnay may baki agr koi unexpected value denga toh it will accept bcuz its dynamic nature like i put one string element.

tup1 : Tuple[str,int] = ("hello",1); 
tup1 = (2,'bye'); # no error

dict1 : Dict[str,str] = { # Dict[keyType,valueType]
    "name" : "John",
}

a :  Union[int,str] = None
# Union[int,str] means a can be either int or str
# but right now as we have set 'None' so if we check methods on 'a' that we can implement so it give both string method as well as integer method.
a="hello" # now it only show string method bcuz i narrow down it.
