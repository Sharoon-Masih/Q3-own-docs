# So basically its a shorthand way to create list on the basis of existing list.

list = [1, 3, 6, 8, 9]

# traditional way
# squaredList = []
# for num in list:
#     squaredList.append(num * num)

# print(squaredList)

# using list comprehension.

squaredList2 = [num * num for num in list] # yaha in first part humnay yeh define krdia kay ko 'num' as variable hum 'for' ma set kia hai usko itself say multiply krka squaredList2 ma store krdo.
# or agay "for num in list" ka mtlb hai 'list' ma jo be individual number get hoga wo 'num' variable ma store hoga.
print(squaredList2)

# e.g
list2 = ['shah','sharoon','aleem','jane','dani']

nameWithS= [name for name in list2 if name.startswith('s')] # so yaha basic for our understanding hum iska flow iss tarah smjh sktay hain kay sab say pehla ek iteration hogi phr at every iteration jo uska agay condition set ki hai wo check hogi or agr wo 'true' return kregi toh 'name' variable ma name hoga at that iteration wo 'nameWithS' list ma store hojyega so iss tarah iska flow create hoga. 

print(nameWithS)