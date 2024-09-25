
try:
    f1= open('1.txt'); 
    f2= open('2.txt'); 
    f3= open('3.txt');
except Exception as e:
    print(e) 

print('create a file that not exist')