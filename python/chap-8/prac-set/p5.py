n = 3
def pattern(n):
    for i in range(n,0,-1):
        for star in range(i):
            print("*",end=" "); 
        
        print("")

pattern(n)