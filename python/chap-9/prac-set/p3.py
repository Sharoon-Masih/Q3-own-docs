# generating tables
def table(n,fileName):
    for i in range(1,13):
        with open(fileName,'a') as file:
            file.write(f'{n} * {i} = {n*i} \n')
    else:
        print(f'Table of {n} is generated and stored in file.')

table(3,'G:/python/chap-9/prac-set/tables/table03.txt')