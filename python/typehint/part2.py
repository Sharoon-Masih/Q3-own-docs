# Type aliases
from typing import List,Dict

myType = List[int] # its a custom type
person = Dict[ # raising error
    str,str,
    str,int
    ]

person1: person = {'name':'shah','age':20}