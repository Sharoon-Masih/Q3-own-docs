
List = ["shah","ahmed","saad","rehman","hamzah","ayub"]
### SORT

List.sort() # by default yeh alphabetical order ma return krega.

# agr reverse order ma chaiya toh bs
List.sort(reverse=True) # toh yeh reverse order ma ayegi.

List1=['irfan','sherry','malik','gujjar','butt',3,4,5]
# List1.sort() # ab yaha par error ayega bcuz mix type ki List ko sort nhi krega , it will only sort the list which is of one type string or number.

# print(List1.sort()); # also remember yeh sort ka func original LIst ma changes krega and in return kuch be return nhi krega.

# also remember sort() func ko case-insensitive bnanay kay lia hum jo 'sort' func may key parameter hai usme 'str.lower' func pass krsktay hain jokay string class ka function hai.

# or basic 'key' parameter may jo be pass kreinga it can be func or anything, wo List ka har element pa apply hogi.

List2 = ["akshay","Mukesh","salman","Katrina"]
List2.sort() # like yeh simple sorting hai joka byb default case-sensitive hai.
print(List2)

# 
List2.sort(key=str.lower) #now ab humna yaha explicitly btadia kay array may jo element hai wo har element pehlay lower case ma change hoga then sorting hogi.
print(List2)

# 
numList = [1,3,6,5,2]
numList.sort() 
print(numList)

#wesa .reverse() ka method be hai jo reverse krdega elements ko.

# resource: https://www.w3schools.com/python/python_lists_sort.asp

### Append (it is like push in js)
# agr hum koi element add krna chahte hain at the end of List ma toh hum append() ko use kreinga.

List3=["harry","muqadas","shareef"]
List3.append("shahid"); 

### insert() 
# To insert a list item at a specified index, use the insert() method.

# The insert() method inserts an item at the specified index:

List3.insert(2,"jason") #ab jo list3 hai usme 2nd index pa "jason" ajayega.But yaha ek sawal haka kya jo iss time 2nd index pa element hai which is "shareef" toh wo replace hojayega? nhi asa nhi hoga wo 3rd index pa shift hojjyaga and jo 3rd index pa element hai wo 4th index pa shift hojayega.

print(List3)

### Extend List
# agr kisi dusri list ma jo elements hain wo saray element jo new list create kr rhay hain usme be chaiya toh hum 'extend' kay method ka through krsktay hain.
akhtarFamily = ["ayub",'akhtar',"Abi","jess","sawera"]; 
gulzarFamily = ["shaleem","aleem","jane","danish","shaheen","jackie"]
gulzarFamily.extend(akhtarFamily) #now ab jo gulzarFamily hai isme akhtarFamily ka be saray element ajagay.

gulzarFamily.sort()

print(gulzarFamily)

### to Remove the List items:

gameList = ["cricket","kuex","football","foosball","snooker","cricket"]

#remove() -> this method will remove the specified item in list. or agr let two or more than two items are same in list toh wo jo item list ma pehla hoga usko remove krega.

gameList.remove("cricket")
print(gameList)

#pop() -> by default it will remove last index of list, but agr hum chahay toh isko explicitly specific index pass kreinga toh srf wohi element remove hoga.

gameList.pop(1); # 1 index pa jo value hai wo remove hojayegi.
print(gameList)

#del -> yeh keyword ka through hum puri list ko be delete krsktay hain or kisi specific index ko be.
del gameList[3]; # remove only element with index 3
print(gameList); 

# del gameList; # it will delete the whole list.

# clear() -> yeh be basicallly list may sa saray element ko remove krdega but isme and 'del' ma yeh farak haka jo del method hai wo puri list ko delete krdeta hai but jo .clear() hai wo list ma jo elements hai just unko remove krta hai puri list ko delete nhi krta which means kay ek ek epmty List bnadeta hai.

gameList.clear()

print(gameList) #it will display empty list [].









