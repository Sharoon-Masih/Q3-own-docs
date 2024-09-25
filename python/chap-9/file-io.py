# basically, in this module we will learn that ho we can manipulate the 'files' through python.

# execution of python program -> basically python ka program RAM pa store hota hai first, then phr machine cycle execute hota hai ab output toh agya but agr hum uss output ko store krna chahay gay toh uska liya humay python ka through uss output ko hard disk ma save krna hoga.

# types of file:
# 1- text file (.txt,.doc etc
# 2- image file (.jpg,.png etc)

# ab agr file ko open krna hai toh open() func use kreinga otherwose for more functionality we can use other funcs.

# There are four different methods (modes) for opening a file:

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists

f = open('test.txt','rt')  # this function takes 2 argument filename and mode, by default 'rt' this mode is set which means that we want to read the text file.

# 1. Relative Paths
# f = open('../sibling_directory/test.txt', 'rt')

# 2. Absolute Paths
# f = open('/path/to/your/file/test.txt', 'rt')

# remember 'rt' ka mtlb haka file ko read kro in text format or wo return be string krega bcuz its text and agr 'rb' toh its mean read file in binary.

data = f.read() # yeh jo method hai it makes the file readable for us convert it in 'str'.
print(data) # we can print data here. 
print(f) # agr hum direct file ko open kreinga toh it is not in readable format.
f.close() # yeh krna lazmi hai, bcuz jab ek dafa file ko open kia hai toh usko close be lazmi hai.

# otherwise the below problem can be occur:

# 1. Resource Leaks
# Each open file consumes system resources. If you open many files without closing them, your program might run out of file descriptors or memory, leading to a resource leak. This can cause your program to crash or behave unpredictably.

# 2. Data Integrity
# When writing to a file, data is often buffered. If you don't close the file, the buffered data might not be written to the disk immediately, potentially leading to data loss or corruption if the program terminates unexpectedly.

# 3. File Locks
# On some operating systems, open files might be locked, preventing other programs or processes from accessing them. Not closing a file can lead to issues with file locks, where other programs cannot read from or write to the file until your program is terminated.