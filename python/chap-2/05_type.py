# type() function and typecasting

# type() function is used to find the datatype of a given variable in python it is same like "typeof" func in JS.

a = 20
print(type(a))
# now it will print type of a which is "int"

# Now why type(a) returns like this <class int>

# In Python, everything is an object, including numbers, strings, functions, and even classes themselves. When you use the `type()` function, it returns the type of the object you pass to it. The type of an object is itself represented as a class in Python.

# ### Why `type()` Returns a Class

# 1. **Object-Oriented Nature**: Python is an object-oriented language, and every entity is an object, including primitive data types like integers and strings. These objects are instances of classes. For example, the number `5` is an instance of the class `int`.

# 2. **Consistency**: Returning a class ensures consistency in how Python handles and describes types. When you call `type()`, it gives you the class that defines the type of the object, maintaining the object-oriented principles.

# 3. **Classes Define Behavior**: Classes define the behavior and properties of objects. By returning a class, Python allows you to inspect and interact with the type's methods and attributes, providing a deeper understanding and control over the objects you work with.

# ### Example

# ```python
# x = 5
# print(type(x))  # Output: <class 'int'>

# y = "Hello"
# print(type(y))  # Output: <class 'str'>
# ```

# In these examples:
# - `type(x)` returns `<class 'int'>`, indicating that `x` is an instance of the `int` class.
# - `type(y)` returns `<class 'str'>`, indicating that `y` is an instance of the `str` class.

# ### Classes and Instances

# - **Class**: A blueprint for creating objects (a particular data structure), containing methods (functions) and attributes (data).
# - **Instance**: A single, unique object created using the class blueprint.

# When you do `type(x)`, Python returns the class that was used to create the instance `x`. For an integer, the class is `int`.

# ### Custom Classes

# You can create your own classes and check their types similarly:

# ```python
# class MyClass:
#     pass

# obj = MyClass()
# print(type(obj))  # Output: <class '__main__.MyClass'>
# ```

# Here, `type(obj)` returns `<class '__main__.MyClass'>`, indicating that `obj` is an instance of `MyClass`.

# ### Practical Implications

# Knowing that `type()` returns the class allows you to utilize class methods and properties dynamically, perform type checks, and implement type-specific behavior in a polymorphic manner.

# ### Example of Using `type()` for Type Checking

# ```python
# def add_one(x):
#     if isinstance(x, int):
#         return x + 1
#     else:
#         raise TypeError("Input must be an integer")

# print(add_one(5))  # Output: 6
# print(add_one("5"))  # Raises TypeError: Input must be an integer
# ```

# In this example, `isinstance(x, int)` checks if `x` is an instance of the `int` class, ensuring type safety.

# By understanding that `type()` returns the class, you can better appreciate Python's object-oriented design and effectively manage and interact with different types of objects in your programs.

# in simple term, python may har cheex object hai primitive data type say leka reference data types tk, which means int,str,boolean etc all are object.

# Typecasting
# ab agr hum kisi variable ki type change krna chahtay hain toh uss concept ko kehtay hain typecasting.
# But python ma Typecasting different hai as compare to TS/JS bcuz TS ma jab hum typecast krtay hain toh wo variable ki actual type ko nhi change krta bs just for removing TS error.
# But in python variable ki actual type change hoti hai.

# int() //yeh convert krga in integer
# str() //convert into string
# float() //convert into float.

# basic yeh jo uper int,str,float yeh constructors hain int,str,float class kay.

a = "31"
print(int(a))  # Convert a number or string to an integer, or return 0 if no arguments

b = 20
print(str(b))

print(float(a)) #Convert a string or number to a floating point number, if possible.

check = True; 
print(str(check)) #agr boolean value ko string ma convert kreinga toh simple value hi ayegi

print(int(check)) # agr boolean value ko number ma convert kray ki koshish kreinga toh wo jo true or false ka picha integer value hai wo ayegi whixh is 0 for false and 1 for true.

print(float(check)) #return 1.0 for true and 0.0 for false.