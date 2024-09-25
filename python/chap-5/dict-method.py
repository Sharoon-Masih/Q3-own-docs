# Dictionary method
a = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

print(a.items()) # yeh ek list return krega jisme basically (key,value) form ma element hongay or unko tuple be kehsktay hain bcuz they are enclosed in () and cannot be change.han isko further manipulate krnay ka liya hum loop wagera ka use krskta hain that we will discuss later on.

print(a.keys()) # this method will return list of keys.
print(a.values()) # this method will return list of values.
print(a.get("city")) # jo key as a arg pass ki hai uski value return hogi otherwise agr wo key exist nhi krti toh phr default value return hojayegi which is 'None' like :
print(a.get("moye")) 

#there is a differencce b/w get() and access item using square notation:
print(a.get("moye")); # iss method ma agr key nhi exist krti toh None ayega. 
print(a["moye"]); # but yaha par keyError ayega agr key nhi exist krti, so its the main difference.

# changing and adding items
a.update({"city":"belgium"}) # it will update the value on the basis of key name.

a.update({"moye":"oye hoye"}) # jo keyName pass kia hai agr wo exist nhi krta dictionary may toh wo as a new key:value add hojayegi dictionary may.

# .update() ko agr print krein toh wo None return krega bcuz wo basic dict ma changes kr rha hai
print(a)

a["name"] = "wylie" # this is another way to change value of key.
a["sex"] = "M" #agr Key nhi exist krti toh wo as a new key:value property add krdega.

print(a)

# for removing item you can check this link: https://www.w3schools.com/python/python_dictionaries_remove.asp