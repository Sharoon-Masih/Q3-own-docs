# Raising exception -> sometimes we want to crash or stop program as well mtlb kay jasay koi game bnai toh uss game different stages hain but ek stage asa aya kay humna program may kaha kay agr yeh wali stage pa user pounch jaye toh bs usko wahi stop krdo he can not continue forward.
n1 = int(input('enter n1: '))
n2 = int(input('enter n2: '))

if(n2 == 0):
    raise ZeroDivisionError('Hey you can not divide by 0 in python') # ab yaha using 'raise' keyword say humnay yeh kia kay jo error occur hoskta tha uski class ko call kia or usme msg be pass krdia.
else:
    print(n1/n2)