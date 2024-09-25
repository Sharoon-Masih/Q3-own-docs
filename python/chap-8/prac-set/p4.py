# Natural numbers are a part of the number system which includes all the positive integers from 1 till infinity and are also used for counting purpose. It does not include zero (0). In fact, 1,2,3,4,5,6,7,8,9…., are also called counting numbers.

def sumOfNaturalNum(n):
    if(n == 0):
        return 0
    return n + sumOfNaturalNum(n-1); # yaha mena yeh logic apply kia kay let say agr n=10 hai toh its means ka jo natural number hongay wo 1,2,3,4,5,6,7,8,9,10 hongay toh jo greatest num hai pehla wo ayega which is 10 + sumOfNaturalNum(9), then 9 + sumOfNaturalNum(8), then 8 + sumOfNaturalNum(7) and so on.

print(sumOfNaturalNum(10))