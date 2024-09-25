set1 = set([1, 2, 3])  # yaha Set create kr rhay hain using Set constructor. Ab set constructor ka through set krnay kay lia basic humay ek list ma value pass krnni hogi(optional syntax).
set1.add(5)
print(set1)
set2 = set(("hello","ok","bye")) # it is also correct and proper syntax.
print(set2)
fruitSet = set(["apple", "cherry", "berry"])
print(fruitSet)

# ----------------------
a = {2,4,6,8}
a.add(8); 
a.add("10")
print(a) # output: {2, 4, 6, 8, '10'} which means ka set ma mulltiple data type ki value/item aa skti hain.

a.remove(4) # yeh remove krdega element ko , but agr element exist nhi krta toh error ajyega.
print(a.pop()) # ab basic yeh jo pop() method hai yeh randomly kisi be element ko remove krskta hai set hai from starting,ending or middle.
# a.clear() # yeh toh set ko clean krdega just empty set will remain

#------Union & intersection--------
a1 = {2,4,6,1}
a2 = {3,7,6,9}

# union of a1 & a2
print(a1.union(a2)) # Now remember yeh ek new Set return krega by merging the above two set ab usme jo same values hain unko as a single value lega and ek order ma return krega.

b1= {'a','c','b'}
b2= {'e','d','f','b'}
print(b1.union(b2)) # in string case wo union toh krdega but sorted order ma nhi hoga return new Set it will be unordered.

#intersection 
print(a1.intersection(a2)) # it will return the common element which exist in both set.
a3 = {10,11,14}
print(a1.intersection(a2,a3)) # we cannot intersect more two set so this is not possible.
#-----------------difference-----------------
print(a1.difference(a2)) # it will return the element which exist in a1 but not in a2. mtlb ka ab jasay jo 'a1' hai isme be '6' hai and a2 mabi '6' toh iss lia 6 return nhi hoga bcuz it is in both.
# there are more methods as well so you should chechk it