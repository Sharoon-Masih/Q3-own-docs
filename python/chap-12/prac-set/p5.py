numList = [1,2,3,4,5,6,7,8,9,10,11,12]
userInput = int(input('enter table no: '))
tableList = [num * userInput for num in numList]
print(tableList)

file = open('tables.txt','w'); 
for num in tableList:
    file.write(str(num) + '\n')