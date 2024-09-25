# Walrus operator

# The walrus operator (:=) is a new feature introduced in Python 3.8 that allows you to assign a value to a variable as part of an expression. It's called the "walrus" operator because the symbol := looks like the eyes and tusks of a walrus.

# walrus operator basically apko allow krta haka you can assign value to variable during expression like here it is in if expression.

# with out walrus operator:
n = len([1,2,3,4,56]) # ab walrus operator pehla n ko value assign krni pari then uspa condition check ki.
if n > 3:
    print('list is greater than 3')

# with walrus operator
if n := (len([1,2,3,4,2])) > 3: # but with walrus op we have done assignment and checking at the same line so it make code short.
    print(f'list is greater than 3 bcuz n = {n}'); # now here a question that why the n = true so answer is below: 

# The walrus operator (:=) is assigning the result of the entire expression (len([1, 2, 3, 4, 2])) > 3 to the variable n. like this n = len([1,2,3,4,2]) > 3 , so ab kiu kay 'len([1,2,3,4,2]) > 3' ka result true ayega toh iss lia n ki value true hogyi.