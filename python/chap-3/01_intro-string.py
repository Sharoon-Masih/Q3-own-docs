# there are 3 ways to write string

firstWay = "string1"
secondWay = "string2"
thirdWay = """Now we can write 
multiple lines in a string, bcuz we 
write in triple quotes"""

# now if we want to access or slice through specific element in string so for that we have use index.

# now basic in python also index start with 0.
# or if we start from the end of string so then index will start from -1 and then -2,-3 and so on, it is bcuz the last index of string is one less than the actual length of string it is like: if string is of 5 character so the last index will be '4' but its length will be 5.

# slicing string
# jasa JS may .slice() method use krtay hain for slicing string or array , isi tarah python may slice krnay kay liya koi method nhi hai bs simple sa syntax hai.
# syntax: string[startIndex:endElementPosition]
myName = "sharoon"
# now there is 7 character in string
slice1 = myName[
    1:4
]  # now it will return 'har' bcuz on the index 1 there is "h" and the '4' is the end index (it is not included) or we can also say the position of that element which we want to extract.

slice2 = myName[:5]  # it will return from 0 to 5th position.

slice3 = myName[2:]  # it will start from 2 index and return the rest whole string.

# Negative Indexing
# Use negative indexes to start the slice from the end of the string:

lastName = "mehboob"
# ab jab negative indexing krtay hain toh uska mtlb hota hai string may last index sa start krna.which means in lastName the last character is "b" so its index will be -1 , then 'o' -2, then '-3' is also 'o' and so on.
print(lastName[-5:-2])  # it will return from '-5' (which is 'h') to '-2' (which is 'o')
print(lastName[-6:6])  # here it will return from 'e' to 'o'.complete word will 'ehboo'.

# formula to find positive index using negative index.
# positive index = totalLength - negative index value.

# e.g
# negative index value = 2 (minus sign iss lia nhi lgya bcuz yaha srf value likhi hai minus already formula may hai agr yaha be lga detay toh phr wo (-)(-) plus hojata.)
# total length = 7
# positive index = 7 - 2 = 5

# slicing with skip value
# syntax: string[startIndex:endElementPosition:skipValue]
# its mean that agr hum chahay toh jo string ka part slice kr rhy hain usme agr value skip krnay ka mechanism lgana hai toh wobi implement hoskta hai.

alphabets = "abcdefghijklmnopqrstuvwxyz"
sliceWithSkip1 = alphabets[0:10:2]
print(sliceWithSkip1)

# let's break it into step:
# first it will return "abcdefghij", then start skipping values from this string.
# it will return 'acegi' , iska mtlb yeh hua kay jo pehla character hai string may wo toh lazmi return krega hi but uskay bd wo value skip krka return krega , ab jasay we have "abcdefghij" isme say pehla wo skip count start krega string ma first character say hi like "ab" then it will print 'c' then skip 'cd' then it will return 'e' then it will skip 'ef' and print 'g' and so on.

# explain the following python code that as the skip value is 2 but its skipping 1 why ? : sliceWithSkip1 = alphabets[0:10:2]
# The Python slice notation you provided, alphabets[0:10:2], has three components:
# 0: This is the start index, meaning the slice begins at index 0.
# 10: This is the stop index, meaning the slice ends before index 10.
# 2: This is the step or skip value, meaning that every second element is taken (i.e., skip one element).

sliceWithSkip2 = alphabets[3:13:3]
print(sliceWithSkip2)
# first it will return :"defghijklm"
# then after skipping it will return: 'dgjm'


