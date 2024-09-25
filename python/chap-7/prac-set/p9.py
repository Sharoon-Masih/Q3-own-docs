# p9

x = 8
for i in range(1,x+1):
    if(i != 1 and i != x):
            print("*",end=""); # by default in print statement there is \n escape sequence, but here we dont want to change line therefore we pass the end argument a empty '' jiska mtlb haka ab print statement ka end pa \n ki jaga empty string hai thats why it will not move to new line.
            print(" " * (x-2),end="")
            print("*",end=""); 
    else: 
        for star in range(x):
            print("*",end=""); 
    print('')