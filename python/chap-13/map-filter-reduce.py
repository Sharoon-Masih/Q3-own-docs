from functools import reduce

# map
# it also accept callBack function in 1st parameter and 2nd parameter it takes list as argument.

l1 = [1, 3, 5, 7, 9, 2, 4, 6]
sqList = map(
    lambda n: n * n, l1
)  # ab yeh jo map method hai yeh object return krta hai and isko proper list may convert krnay ka liya we to do like this list(sqList).
properSqList = list(sqList)
print(properSqList)


# filter
# it also accept callBack function in 1st parameter and 2nd parameter it takes list as arguments.
def findEven(n: int) -> int:
    if n % 2 == 0:
        return True
    return False


evenFilterObj = filter(findEven, l1)
evenList = list(evenFilterObj)
print(evenList)

# reduce
# basic jo reduce ka function hai wo import krna parta hai functools say:
sumOfList = reduce(lambda a, b: a + b, l1)
print(sumOfList)
subtracList = reduce(lambda a,b : b - a,l1)
print(subtracList)
