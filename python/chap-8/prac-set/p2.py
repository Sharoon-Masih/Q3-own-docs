inputTemp = float(input("Enter temp in Celsius: ")); 

def tempCtoF(tempInC):
    # tc = 5/9 * (tf - 32)
    farenheit = ((9 * tempInC) / 5) + 32
    return farenheit;

print(tempCtoF(inputTemp))