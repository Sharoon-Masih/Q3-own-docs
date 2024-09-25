factNum = int(input('Enter the num you want factorial of: '))

fact  = 1
formatStr = ' '
for i in range (factNum,0,-1):
    fact *= i; 
    if (i > 1):
        formatStr += f' {i} *'
    else:
        formatStr += f' {i}'

print(formatStr + ' = ' + str(fact))