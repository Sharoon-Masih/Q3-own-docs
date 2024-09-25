li = ["shah", "yasir", "faryal", "al"]


def removeWordFromL(list, word):
    finalList = []; 
    for item in list:
        if(item != word):
            finalList.append(item.strip(word))
    
    return finalList

print(removeWordFromL(li, "al"))
