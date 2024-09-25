# try - else

# acha sometime kuch asay senerio hotay hai jaha par hum chahaty hain kay kuch specific code srf tab hi execute ho jab try ka block successfully run hojaye.
# so for achieving that point i can use 'else'.

try:
    x = 5 / 2

except:
    print("An error occurred")
else:
    print("divided succesfully")  # agr try block execute hoga toh yeh else chlega otherwise agr 'except' block execute hoga toh yeh 'else' block be nhi chlega. 