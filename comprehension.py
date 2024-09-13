# provide a concise way to create sequences like list,dictionary or sets
# comprehensions are more readable and efficient than traditional loops
#shorter and less lines of code

#..........................LIST COMPREHESIONS.....................

#Traditional List
fruits = ["apple", "banana", "orange", "cherry", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

#syntax
# --------> syntax = [expression for item in iterable if condition]

#List comprehension 
fruits = ["apple", "banana", "orange", "cherry", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

lengths = [len(fruit) for fruit in fruits]
print(lengths)

#.....................DICTIONARY COMPREHENSION..........................

#traditional Dictionary
fruits = ["apple", "banana", "orange", "cherry", "mango"]
fruit_length = {}

for fruit in fruits:
    fruit_length[fruit] = len(fruit)
print(fruit_length)

#syntax
# -----------> {key_expression: value_expression for item in iterable if condition}

#List comprehension
fruits = ["apple", "banana", "orange", "cherry", "mango"]
fruit_length = {fruit: len(fruit) for fruit in fruits}

print(fruit_length)

#.....................SET COMPREHENSION..........................

#traditional set
fruits = ["apple", "banana", "orange", "cherry", "mango"]
fruit_lengths = set()  # Initialize an empty set

for fruit in fruits:
    fruit_lengths.add(len(fruit))  # Add the length of each fruit to the set

print(fruit_lengths)

#syntax
# ----------->  {expression for item in iterable if condition}


#comprehension set
fruits = ["apple", "banana", "orange", "cherry", "mango"]
fruit_lengths = {len(fruit) for fruit in fruits}
print(fruit_lengths)


#.....................GENERATOR COMPREHENSION..........................

#traditional generator
numbers = [1, 2, 3, 4, 5]
def square_generator(nums):
    for num in nums:
        yield num * num  # Yield the square of each number
gen = square_generator(numbers)
for square in gen:
    print(square)

#syntax
# -----------> (expression for item in iterable if condition)

#comprehension generator
numbers = [1, 2, 3, 4, 5]
gen = (num * num for num in numbers)

for square in gen:
    print(square)
