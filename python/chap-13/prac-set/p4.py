from functools import reduce

rawList = [2, 3, 4, 1, 5, 6, 7, 4, 2, 32, 13, 14, 25, 30, 54]

dividedBy5 = filter(lambda n: n % 5 == 0, rawList)
print(list(dividedBy5))


# p5
def maxInt(a, b):
    if a > b:
        return a
    else:
        return b


maxNum = reduce(maxInt, rawList)
print(maxNum)
