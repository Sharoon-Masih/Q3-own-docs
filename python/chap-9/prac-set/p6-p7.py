with open("p6.txt") as f:
    content = f.read()
    if "python" in content:
        print("Python is mentioned in the file")
    else:
        print("Python is not mentioned in the file")

# p7
with open("p6.txt") as fileCheck:
    line = fileCheck.readline()
    lineNo = 1
    while line != "":
        if "python" in line:
            print(f"python is written on line {lineNo}")
            break # break iss lia kia hai taka jasay hi line get ho loop terminate hojaye.
        lineNo += 1
        line = fileCheck.readline()
