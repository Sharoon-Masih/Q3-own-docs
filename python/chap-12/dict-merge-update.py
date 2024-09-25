# Dictionary merge and update operators

# by using the | sign we can merge dictionaries.

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

dict3 = dict1 | dict2 # also remember, it will take same property as common ab jasay b is in both dict1 & dict2, but jo value hai wo dict2.b ki print hogi bcuz while merging jo dictionary last ma hogi uski preference zeada hogi like here it is dict2. 
print(dict3)
dict4 = dict2 | dict1; # dict1 has more preference.