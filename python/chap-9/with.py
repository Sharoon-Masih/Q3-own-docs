# 'with' statement 
# now basically as we know jab be file open krni hai toh usko close be lazmi krna hai which become hectic or sometime we forget so to remove this burden we will use 'with' statement. 
with open('test.txt','rb') as f: # 'rb' mode mena jaan bhuj kay check krnay ka liya set kia wesa its mean that kay our file will be read in binary format.
    print(f.read())

# now we dont need to close file it will be closed automaticaly when we come out of 'with' statement.