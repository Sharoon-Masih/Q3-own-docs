file = open('test.txt','r')
# data = file.read(5) # it will return only the first 5 chracter in file.
# print(data)
# file.close(); # remember agr ek file ek dafa close krdi or after closing statement agr uss same file pa koi manipuation kreinga toh it arise error.


# Readline (for reading oneline at a time)
onelineData=file.readline()
print(onelineData)

# # By calling readline() two times, you can read the two first lines:

# print(file.readline()) #line 1

# print(file.readline()) #line 2 # ab agr humari file srf 2 lines hain jo jab hum line 3 print kr rhay hain toh tab kya hoga toh basically at that time wo srf ek '' empty string return krega so isilia agr hum jitni dafa extra readline kreinga wo ek empty string return krega at new line. 

# print(file.readline()) #line 3


#By looping through the lines of the file, you can read the whole file, line by line.
line = file.readline(); 
while  (line != ''): # yaha condition set krdi kay line equal to empty string hojaye toh loop hojaye.
    print(line); # yaha print hoga.
    line = file.readline() # or yaha after each iteration line variable ko next line assign kr rhay hai from the file.  

# Readlines method (it return a list of line at once)
file.close()

# ----------------------------
# Write to an Existing File
# To write to an existing file, you must add a parameter to the open() function:

# "a" - Append - will append to the end of the file

# "w" - Write - will overwrite any existing content

file2 = open('test.txt','w'); # before performing any operation must remember to open file in correct mode.
newWrite = file2.write('i have overwrite the new text')
# yeh method puri file ko overwrite krdega means jo be pehlay text hai usko replace krka new text add krega.
#remember iss method ko new text dena lazmi hai and agr iska output print krein toh yeh in return number of character retrurn krega jo add huye hain.

# print(file2.read()) # it raises bcuz jo file open hui hai wo 'w' write mode ma hui hai agr uspa koi or method apply kreinga toh error ayega.
file.close()

# append
file3 = open("test.txt", "a")
file3.write("Now the file has more content!")
file3.close() 

# ab agr hum chahtay hain kay existing file ma kuch new add krna toh uskay lia we will use append, by just adding 'a' in mode while opening file.

# ---------------------------------
# Create a New File
# To create a new file in Python, use the open() method, with one of the following parameters:

# "x" - Create - will create a file, returns an error if the file exist

# "a" - Append - will create a file if the specified file does not exist

# "w" - Write - will create a file if the specified file does not exist