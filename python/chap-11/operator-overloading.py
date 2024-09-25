# class Number:
#     def __init__(self,num):
#         self.num=num; 


# n1 = Number(2);
# n2 = Number(3);
# print(n1.num + n2.num);  # hum iss tarah be add krsktay hain but iska proper way hai by using operator overloading.

# 
class Number:
    def __init__(self,num):
        self.num=num; 

    def __add__(self,num): # ab yeh jo dunder method bnaya hna yeh automatically run hojayega on the basis of operator like in at line 19 mena 'n1.num+ n2.num' iss tarah sa add nhi kia blka direct 'n1 + n2' krdia toh usme jo operator lgya hai usse usne judge krlia kay '__add__' method ko invoke krna hai isi tarah later on jab hum __multiply__ create krenga toh usme wo '*' ka through judge krlega.
        return self.num + num.num # acha isme jo 1st parameter hai wo toh chlo thk hai jo first instance of class hoga uska 'num' get krlega or 2nd parameter lgya hai wobi iss lia lgya hai bcuz jo second instance hai wobi hai toh 'Number' class ka hi instance toh iss lia usko be get krnay ka liya ek random parameter named as 'num' liya you can set any name but usme jo '.' ka through property access krni hai uska name correct hona chaiya which is 'num' in our case, bcuz agr ap 'NUmber' class constructor jo attribute create ho rha hai uska name 'num' hi hai.
    

    # multiply 
    def __mul__(self,num): # also remember function name should be correct bcuz its a convention. like agr ma 'mul' ki jaga 'multiply' krdeta toh error ata.
        return  self.num * num.num
    
    # subtraction 
    def __sub__(self,num): 
        return  self.num - num.num
    
n1 = Number(3)
n2 = Number(5)
print(n1 + n2 )  # ye humari add operation hai jo humne operator over
print(n1 * n2)