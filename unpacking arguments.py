# the process of taking a packed tuple or dictionary or list and unpacking its elements into separate variables
# unpacking arguments using the * and ** operators

#Unpacking Positional Arguments (*)
# --> * allows you to pass a list or tuple of values into a function as individual arguments.
def add(x, y, z):
    return x + y + z

numbers = (1, 2, 3)  # A tuple with three numbers
result = add(*numbers)  # Unpacks the tuple into 1, 2, and 3
print(result) 


#Unpacking Keyword Arguments (**)
# ----> ** lets you pass a dictionary of values into a function as named (keyword) arguments.
def greet(name, age):
    return f"Hello {name}, you are {age} years old!"

info = {"name": "Alice", "age": 30}  # A dictionary with name and age
message = greet(**info)  # Unpacks the dictionary into name="Alice" and age=30
print(message) 


# Combining Positional and Keyword Arguments
# ---> we can use both * and ** together to pass both lists/tuples and dictionaries to a function.
def describe_pet(name, age, species="dog"):
    return f"{name} is a {age} year old {species}."

args = ("Max", 5)  # A tuple with name and age
kwargs = {"species": "cat"}  # A dictionary with species

description = describe_pet(*args, **kwargs)  # Unpacks both tuple and dictionary
print(description) 

#Using Unpacking in Function Definitions
# ----> we can define functions that accept any number of positional or keyword arguments using * and **.
def print_info(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

print_info(1, 2, 3, a="x", b="y")

# *args collects all positional arguments into a tuple (1, 2, 3).
# **kwargs collects all keyword arguments into a dictionary {'a': 'x', 'b': 'y'}.

#unpacking with List comprehensions
pairs = [(1, 'one'), (2, 'two'), (3, 'three')]  # A list of tuples
result = [f"{num} is {word}" for num, word in pairs]
print(result)  
 