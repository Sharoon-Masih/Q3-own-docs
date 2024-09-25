# basic type hint

n: int = 2
n = "" # no error

# so basically python 3.8 ma jo by default type hint mili hai yeh asa nhi kay python ki jo dynamic nature usko khtam krdeingi NO, yeh srf suggestion hain for developer kay explicitly ek variable ko jab koi type define krdi toh it instruct developer kay assign value to it A/C to its type.
# and on the other hand ab kiu kay 'n' ki explicitly type 'int' set krdi hai toh wo jo method ki intellisense provide krega wo srf integer walay method hi hongay.
# But agr hum yeh sochay kay jasay 'n' ki type int hai or agr hum usko string value assign krenga toh runtime pa ya compile time pa error ayega toh asa nhi hai.
# also remember agr hum chahtay hain kay nhi we want static typing mtlb jisme python will not allow us to assign other value rather than its type, so then we have to use 'mypy' tool of python.


# function type definition:
def greet(name:str,age:int) -> None :
    print(f"Hello {name} you are {age} years old")
    # remember yaha be jo type define ki hain wo just suggestion dengi baki agr hum chahay toh 'name' int value be pass krsktay hain and secondly jasa here we set return type of func 'None' which you can think like 'avoid' in other languages.
    # function ki return type 'None' toh set krdi but agr hum string return be kreinga toh error nhi ayega bcuz these types are only for guideline.