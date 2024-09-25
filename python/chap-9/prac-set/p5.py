
wordToBeRemove = ["donkey","ganda","bad"]
with open('p4-file.txt') as f:
    text = f.read()
    newText = text; 
    for word in wordToBeRemove:
        newText = newText.replace(word,'#' * len(word))

with open('p4-file.txt','w') as makingChangesInFile:
   makingChangesInFile.write(newText)

