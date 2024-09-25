# Tuple -> tuple are also lilke list bs difference yeh haka tuple immuteable hotay hain.

# which means once tuple create hogya usme na koi element add hoga or na hi koi change hoskta hai.in other words we can also say that it is collection of constants.

# tuple ko create krnay ka liya hum jasa list ka liya [] brace lgatay hain tuple ka liya () brace lganay hain.

Tuple1= ("apple","banana","cherry","chikko")

# Tuple1[0] = "mango" #error -> cant change it.

print(Tuple1[0]) # return apple.

# agr koi yeh ques kray ka kia tuple ma unlimited elements add hosktay hain? toh uska answer yeh haka at the time of initialization toh hosktay hain likin bd ma nhi hosktay.

emptyTuple=()
print(emptyTuple) #print empty tuple.

# Allow Duplicates -> its mean kay ek tuple may same elements hosktay hain

Tuple2 = ("ball","bat","ball") # acceptable.

# tuple can contain element of different type as well.

multiTuple = ("jack",1,2,3,"paul",False)

print(multiTuple)

# Tuple of one Item -> mtlb kay agr srf one item ka tuple create krna ho toh wo kasa hoga .

singleItemTuple = ("alen") # it will not consider tuple it is simple string, wo iss lia bcuz remember jab be tuple create krna hai jisma just single item hoga toh usme after writing item must put "," .

print(singleItemTuple)

correctTuple = ("walker",) # now it is a tuple.

### Tuple methods 

## mainly we can apply two methods on tuple.

print(multiTuple.count(2)) # it will return number of count that jo '2' element hai yeh kitni dafa aya hai multituple may. 

print(multiTuple.index("jack")) #yeh jo index method hai yeh uss element ka index number return krega agr jo value pass ki hai wo tuple ma exist krti hai otherwise error return hoga.

# ---------------------------------------

# In Python, tuples are immutable sequences, which means their elements cannot be changed after they are created. Because of this immutability, tuples have fewer methods compared to lists. Here are the methods available for tuples:

# 1. **count()**: Returns the number of times a specified value appears in the tuple.

#    ```python
#    my_tuple = (1, 2, 3, 2, 2, 4)
#    count_of_twos = my_tuple.count(2)
#    print(count_of_twos)  # Output: 3
#    ```

# 2. **index()**: Returns the first index of a specified value. If the value is not found, it raises a `ValueError`.

#    ```python
#    my_tuple = (1, 2, 3, 4, 5)
#    index_of_three = my_tuple.index(3)
#    print(index_of_three)  # Output: 2
#    ```

# These are the only methods specific to tuples in Python. However, you can also use built-in functions that work with any iterable, including tuples:

# - **len()**: Returns the number of items in the tuple.

#   ```python
#   my_tuple = (1, 2, 3, 4, 5)
#   length = len(my_tuple)
#   print(length)  # Output: 5
#   ```

# - **min()**: Returns the smallest item in the tuple.

#   ```python
#   my_tuple = (1, 2, 3, 4, 5)
#   minimum = min(my_tuple)
#   print(minimum)  # Output: 1
#   ```

# - **max()**: Returns the largest item in the tuple.

#   ```python
#   my_tuple = (1, 2, 3, 4, 5)
#   maximum = max(my_tuple)
#   print(maximum)  # Output: 5
#   ```

# - **sum()**: Returns the sum of all items in the tuple (all items must be numbers).

#   ```python
#   my_tuple = (1, 2, 3, 4, 5)
#   total = sum(my_tuple)
#   print(total)  # Output: 15
#   ```

# - **sorted()**: Returns a sorted list of the tuple's elements.

#   ```python
#   my_tuple = (3, 1, 4, 2, 5)
#   sorted_tuple = sorted(my_tuple)
#   print(sorted_tuple)  # Output: [1, 2, 3, 4, 5]
#   ```

# - **in**: Checks if an element is present in the tuple.

#   ```python
#   my_tuple = (1, 2, 3, 4, 5)
#   is_three_present = 3 in my_tuple
#   print(is_three_present)  # Output: True
#   ```

# - **tuple()**: Converts an iterable to a tuple.

#   ```python
#   my_list = [1, 2, 3, 4, 5]
#   my_tuple = tuple(my_list)
#   print(my_tuple)  # Output: (1, 2, 3, 4, 5)
#   ```