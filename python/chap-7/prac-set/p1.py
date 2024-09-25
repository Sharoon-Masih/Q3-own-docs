tableNum = int(input("enter table num: "))

for x in range(1, 13):
    print(f"{tableNum} * {x} = {tableNum * x}")
else:
    print(f' table of {tableNum} from 1 - 12')