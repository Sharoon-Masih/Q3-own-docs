# primarily in python we have 2 types of loop:
# 1. for loop
# 2. while loop

# While loop syntax 

# while condition:
    # code to be executed

# e.g 1
i = 0
while  i <= 4 : 
    print(i); 
    i+=1 #as we are working with while loop so here we set condition 'i less than or equal to 4' toh ab agr yaha par 'i' ma increment nhi kregay toh toh while loop ma jo condition hai wo kabhi true nhi hogi and loop will become infinite. 

# for loop
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

# Acha in normal languages the 'for' loop is used differently mtlb kay waha humay for loop may 3 conditions deni hoti hai initial value ; final condition ; incre/decre value but in python for basically work like '.map()' method in JS jasa usko hum array,object ko iterate krnay ka liya use krtay hain. isi tarah say python ma 'for' ko list,tuple iterate krnay ka liya use krtay hain.other than that we can also apply range function.

Fruits = ['apple','cherry','banana']; 
for fruit in Fruits:
    print(fruit)   

# Looping through a string 
str1 = 'hey sharoon'
for s in str1: # 's' variable may ek single character ayega from the above string at each iteration.
    print(s)

# Looping through a dictionary
dict = {
    'name' : 'sharoon',
    'age' : 20
}
for key in dict: # jab hum dictionary ko iterate krtay hain toh jo variable hum set krtay hain like here we set 'key' toh usme dictionary ma jo 'keys' hoti hain wo hi ati hain at each iteration agr humay uss specific key ka against koi value chaiya toh that we can also get like below. 
    print(f'{key}:{dict[key]}')

# in same way we can also iterate through 'Set'.

# Break statement
cityList = ['karachi','lahore','isl','hyd','quetta']

for city in cityList:
    print(city)
    if(city == 'hyd'):
        print('stop here!')
    print('done') #note the difference basically yeh jo print statement hai iska if block sa koi taluk nhi hai which means that it is out if its scope but agr ma isko be indent krdo ga toh phr yeh if block ma ajagi.Ab kiu kay yeh wali statement if block ma nhi hai toh iss lia it will execute everytime until the loops end.

# now using break statement
for city in cityList:
    print(city); 
    if( city == 'hyd'):
        print('stop here!'); 
        break; # now ab yeh jo break ki statement hna toh iska mtb yeh haka ab jasa hi yeh break statement execute hogi toh pura jo block of loop hai wo terminate hojayga ,which means jo isse nichay wali statement hai wobi execute nhi hogi.
    print('done')

# Continue statement
cityList = ['karachi','lahore','isl','hyd','quetta']
for city in cityList:
    print(city)
    if(city == 'hyd'):
        print('arrived')
        continue # ab jo continue statement hai usme yeh hota hai kay jasa break statement toh puray loop ko hi terminate krdeti hna but jo 'continue' statement hai wo just current iteration ko stop krti and next iteration krti hai. mtlb kay ab jasay hi yaha hum if block set kia hai jab 'hyd' ayega toh print hoga 'arrived' and uskay sth hi 'continue' statement be execute hojayegi which means ka jo abhi current iteration hai isko terminate krdo and jo next iteration hai uspa move hojao which is 'quetta'.
    print('done')

# pass statement 
for city in cityList:
    if(city == 'isl'):
      pass # pass ka mtlb hota hai "Do nothing" mtlb ka kuch bhi nhi hoga.its a null statement
    print(city) 

# for loop with else statement
sports = ["cricket",'football','hockey']

for sport in sports:
    print(sport)
else:
    print('these are games we can play!')

# ab basic yeh jo 'else' hna yeh srf tab execute hoga jab complete loop end hojayega.But jab tk loop chlta rahega yeh execute nhi hoga. 

# The else block will NOT be executed if the loop is stopped by a break statement.