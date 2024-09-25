with open('p4-file.txt') as f:
   text = f.read()
   newText = text.replace('donkey','######')
with open('p4-file.txt','w') as makingChangesInFile:
   makingChangesInFile.write(newText)

