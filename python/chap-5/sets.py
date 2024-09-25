# Set ->

#syntax
Set = {1,2,3} # set ko create krnay ka liya hum curly braces ka use krtay hain but on the other hand hum dictionary be curly braces say bnatay hain.

# toh agr ek empty set create krna hoga toh wo kasa hoga.
a = {} # agr iss tarah sa kreinga toh yeh toh ek empty Dict ban jayegi.
s = set() # so for empty set we will use 'set' class cnstructor .

# Now why we need to use Set ?
# ab basic jo set hai usko hum mainly tab use krtay hain jab hum chahtay hain kay jasay humaray pass ek large collection of elements hai ab usme bht saray element same hain but hum chahtay hain ka collection may jo same element hain wo remove hojaye mtlb kay agr 5 three times aa rha hai toh wo just one time hojaye toh in that situation we can use 'set'.
# also remember set is a unordered collection which means ka set ma hum sorting wagera nhi krsktay hain uska lia phr humay 'list' use krni hogi.
# set are immutable which means ka hum existing set ma change nhi krsktay.
# but hum set ma item add and remove krsktay hain.
# or jab humay union,intersection etc iss tarah ka operation perform krnay hotay hai toh tab be hum set ka use krty hain.

set1 = {1,2,4,5,5,5,6}
print(set1,type(set1))

set2 = {1,True,0,False} # also remember '1 and True' dono same consider hongay and same as '0 and False' be same consider hongay.
print(set2) # here it will print 1, 0 