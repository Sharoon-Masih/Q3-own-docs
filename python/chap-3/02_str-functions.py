sentence ="hey i am a jamstack dev"

print(len(sentence)) #it will return the length of string, also count white spaces as well.
print(sentence.endswith('ev')) #it will return true if the string is ending with 'ev'.
print(sentence.endswith('ev ')) # remember it will notice white spaces also ab jasay jo uper string hai usme toh white space nhi hai last may but yaha par endswith ma dia hai toh wo yebi count krega.
print(sentence.endswith('Ev')) # it will return false bcuz it is case-sensitive.

print(sentence.startswith('he')) # all rules are same like endsWith.
print(sentence.count('c')) # it will count that how many times the input character represent in given string.it is also case sensitive.
print(sentence.count('abc')) # ab yaha par yeh nhi kay wo just for specific character ka liya check krega mtlb kay jasay ab jo argument pass kia hai wo specific character nhi blka ek word ki tarah hai toh wo uss word ki occurence checkk krega kay yeh pura word kitni dafa appear hua hai string may.
print(sentence.capitalize()) # it will capitalize the first letter in the string.
print(sentence.title()) #it will convert string into title case, which means string ma jitnay be words hongay unka first letter capital krdega.
print(sentence.upper()) # make whole string uppercase
print(sentence.lower()) # make whole string lowercase
print(sentence.find("dev")) # yeh string ma check krega kay yeh character ya word exist krta hai toh uska index numbers return krdega. or jasa agr ek word hai toh uska jo first letter ka index num hoga wo return krega like here 'dev' word ma jo first letter hai 'd' uska index num '20' toh just wo return krega agr 'dev' word exist krta hoga string ma toh.
print(sentence.replace('dev','developer')) # yeh jo method hai yeh jo be word ya chracter pass kreinga usko replace krdega new word sey, but remember jo original string hai yeh usma koi changes nhi layega wo jasa hai wo wesa hi rahegi.
print(sentence.replace('e',"a")) #ab yeh puri string may jaha 'e' hai usko replace krdega 'a' sey.

# you can check more method on chatgpt
print(sentence); # most important thing to understand that jitnay be method humna uper apply kia hain wo original string pa koi be effect nhi dalegay.  

# remember strings are immuteable in python isi lia koi be method uspa apply kreinga toh original string ma changes nhi krega.