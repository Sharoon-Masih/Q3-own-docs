list = ['cake','biscuit','drink','pizza']

index = 0
for item in list:
    print(f'the item at index {index} is {item}')
    index +=1; 

# ab ek way toh yeh hai agr hum har item ka corresponding 'index' chaiya toh iss tarah krsktay hain but iska proper way is below:

for index,item in enumerate(list): # toh yaha humna easily 'enumerate' function use krkay jo iska pehla 'index' return hoga and 'item' may jo list item hai wo return hojayegain.
    print(f'the item at index {index} is {item}')