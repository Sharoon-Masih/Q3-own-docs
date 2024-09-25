# The range() Function

# To loop through a set of code a specified number of times, we can use the range() function.

# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

# mtlb ka jasay in normal languages hum 'for' ma number of loop specified krtay thy like this for (i=0; i < 4; i++)  toh yeh kam python ma krnay ka liya we can use range fuction.

# syntax 
# range(start, stop, step)
# start: The starting number of the sequence. Default is 0.
# stop: The end value of the sequence. This is exclusive, which means the stop value will not print
# step: step means kay at each iteration hum kitnay ka increment/decrement krna chahtay hain by default 1 hai.

for x in range(6): # ab basic jo start and step wala parameter hai wo optional hai but jo stop hai wo requirerd hai toh iss lia yaha humna 6 put kia hai uska mtlb hai yeh code 6 time iterate hoga.
    print(x) #or basic yeh range func ki start value by default '0' hai and as we know kay jo stop value put krtay hain usse less than 1 tk chlta hai mtlb kay here we put 6 which means ka yeh ab chlega srf 5 tk. 0 to 5

for x in range(1,6): # yaha par jasay humna khud say start value provide ki hai that is 1 tohh its mean now loop will run from 1 to 5 
    print(x) 

print('-------------------')
for i in range(2,7,2): # now here it will start fromm 2 then increment by 2 and it become 4 then again incre by 2 and it become 6 and then terminate bcuz the stop range is 7.
    print(i)

print('----------------')
for i in range(7,2,-1): # ab yaha hum descending order ma execute kr rhay hain where range start hogi 7 say and kiu jo stop hai wo 2 hai thats why the last number will be 3 kiu kay jo stop value hoti hhai wo include nhi hoti. and '-1' means at each iteration there will be decrement of 1.
    print(i)