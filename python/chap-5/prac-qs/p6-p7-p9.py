favLang = {}; 
frd1Name = input('enter ur name: '); 
frd1Lang = input('enter ur fav Lang: '); 
favLang.update({frd1Name:frd1Lang}) 
frd2Name = input('enter ur name: '); 
frd2Lang = input('enter ur fav Lang: '); 
favLang.update({frd2Name:frd2Lang}) 
frd3Name = input('enter ur name: '); 
frd3Lang = input('enter ur fav Lang: '); 
favLang.update({frd3Name:frd3Lang}) 
frd4Name = input('enter ur name: '); 
frd4Lang = input('enter ur fav Lang: '); 
favLang.update({frd4Name:frd4Lang})

print(favLang)

#q7- agr more than one friend ka name same hoga toh kya hoga?
#ans- agr more than one friend ka name same hoga toh dictionary may wo add nhi hoga blka update hojayega bcuz jo update method wo yehi krta hai kay agr toh key already dict ma ho th update krdega else as a new property add krdega.

#q8- but agr more than one friend ki language same hogi toh phr be koi affect hoga dict pa ya nhi ?
# Toh agr language ki value change hogi toh koi affect nhi hoga bcuz its value not key. 

