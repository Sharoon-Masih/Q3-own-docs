# its a QS-4 program, where i have to print the content of directories.

import os; #here simply yeh built-in mmodule import kia.

directory_path ="/python" #yaha jis directory ka content chaiya wo uska path store kia.or remember jis drive sa data ayega 

contents = os.listdir(directory_path); #and here the listdir will list the directories include in the path we mention.

for item in contents: # or kiu kay yeh jo 'contents' isme array ki form ma data ayega usko bs loop krdia.
 print(item)