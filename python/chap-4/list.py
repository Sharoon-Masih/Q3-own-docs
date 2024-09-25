# List are like array in  python . they can contain different type of elements.like string,int etc

myList1= ["shah","sharoon","rufen",55,False] # here you can see this list is of mix element.
print(myList1) # this will print the list.
print(myList1[0]) # this will print the first element of the list.

# Now here is something shocking
name = "sharoon masih"
# name[0] = "e" #now here you will see that you cant change in string bcuz it is immuteable.
print(name)

list1 = ["shah","ali","hunara","shamsher","jamshed"]; 
# list1[0] = "shahar"; #here you will see that list1 may changes hojayega.this proves that arrays or list are muteable.

# yehi difference hai primitive types may and reference types, mtlb kay jo string,boolean,integer yeh primitive types hain and yeh immuteable hain but jo reference type array,obj etc hain wo muteable hain.  

# Now remember length,slicing find krnay ka method,technique same hi rahegi.
# print(len(list1)); 
# print(list1[1:4]); # now it will return from index 1 to 4th position element.
print(list1[0:4:2]) 
# first it will return ["shah","ali","hunara","shamsher"]
# then, it will start skipping 2 elements so final result will be like: ["shah","hunara"] //first element toh ayega hi array ka, phr 2 count krega which is like "shah" and  "ali" and then jo 3rd element hai wo ayega "hunara" , then phr 2 count krega which is like "hunara" and "jamshed" or phr uska bd agay array ma koi element nhi hai iss lia final result ["shah","hunara"].

list2 = ["sharoon","aleem","danish","shaheen","shaleem"]
list2[0:3] = ["amir","bunny"]
print(list2) # ab yeh jo list2 hai yeh isme jo list2[0:3] isko jitny replace hojayega or uski jaga humnay agay element assign kia tha or wohi ajagay. but ab jasay list2[0:3] toh isme toh 3 elements extract kr rhay hain toh jo bs wohi element change hongay jitnay assign kreinga. 

# resource: https://www.w3schools.com/python/python_lists_change.asp

# remember in python we can only access list member using indexes, we cannot access them be name like this:
list2["ali"]