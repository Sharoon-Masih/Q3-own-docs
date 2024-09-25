candidateName = input("Enter your name: "); 
letter = ''' Dear <|NAME|>,\n\tYou are Selected!\n\t<|DATE|>'''

filledTemplate = letter.replace("<|NAME|>",candidateName.capitalize()).replace("<|DATE|>","10/11/2024") #here first i replace name and then jo new string replace na return ki uspa further replace lga kay date ko bhi krdia replace.

print(filledTemplate)