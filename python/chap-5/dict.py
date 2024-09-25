# Dictioaries (dict) -> it is also a collection, but here we can store data in key:value pair its same like 'object' in JS.

# ab basic kisi individual person ki multiple properties/element ek collection ma store krnay hain toh we will use dictionary , yeh hum list ka through be krsktay hain but it will become complex and also it require more computational power.like:
std = [
    ["shah", 20, "M"],
    ["harry", 25, "M"],
]  # ab jasay yaha humna list of list create krli or we can say 2d list, but ek toh msla yeh haka yaha hum key name ka through value nhi access krsktay we have to use index and secondly agr koi complex logic krtay hain toh it require more computational power.

# syntax:
book1 = {
    "name": "Harry Potter",  # remember key should be marked in double quotes.
    "author": "Harry",
    "release": 2000,
    "additions" : [1,2,3,4]
}

book2 = {} # empty dictionary

# above we created book1 dictionary

# printing & checking type of book1
print( book1, type(book1))

# accessing dictionary element
print(book1["name"]) # it will print name.
print(book1["additions"]) # it will print additions list

List = book1["additions"]
# print(" ".join(List)) # here you will see that when i am trying join the list which we get from book1 dictionary but its not joining it.iski waja yeh haka kiu kay jo humari List ma element hain wo string literals nhi hain they are integers thats why first we have to convert it in string and then apply join().
print(type(List))

# Properties of dictionaries
# 1. ordered collection of key-value pairs (iska mtlb hai kay pehla jab properties dictionary ma stre hoti thi toh wo order wise nhi hoti thi mtlb kay jo pehla hui wo first then 2nd then 3rd and so on also known as unordered. but after python 3.7 version now properties are stored in sequence/order)

# 2. mutable (it mean we can make changes in existing dict)
# 3. key cannot be duplicate (same name key will not be acceptable)
# 4. indexed (its mean ka jasay list humay khud say index number wagera ka through access krni parti hai value yha already keys ka through indexed hai just we have use key name to access value.)

# 5. key can be string,interger,float

