inputNum1 = input('Enter num 1: ');
inputNum2 = input('Enter num 2: ');
inputNum3 = input('Enter num 3: ');
inputNum4 = input('Enter num 4: ');

if (inputNum1 > inputNum2 and inputNum1 > inputNum3 and inputNum1 > inputNum4):
    print("The largest number is", inputNum1); 
elif (inputNum2 > inputNum1 and inputNum2 > inputNum3 and inputNum2 > inputNum4): 
    print("The largest num is ", inputNum2)
elif (inputNum3 > inputNum1 and inputNum3 > inputNum2 and inputNum3 > inputNum4): 
    print("The largest num is ", inputNum3)
elif (inputNum4 > inputNum1 and inputNum4 > inputNum2 and inputNum4 > inputNum3): 
    print("The largest num is ", inputNum4)
else:
    print("All numbers are equal")