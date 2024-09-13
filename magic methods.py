# also known as dunder methods
# start and end with double underscores(__init__)
# used to define the behaviour of objects for various built-in operations and functions

#commonly used magic methods.
 
# 1. INITIALIZATION 
# ----> sets up an initial state of an object when it's created
class Person:
    def __init__(self, name, age): # self is the reference instance to person ; name and age are parameters 
        self.name = name
        self.age = age

# Creating an instance of Person
person = Person("Alice", 30)


# 2. REPRESENTATION
# ----->  provide a string representation of the object
class Person:
    def __repr__(self): #python calls to get a string representation of the object
        return f"Person(name={self.name}, age={self.age})"

person = Person("Alice", 30)
print(repr(person)) 

#COMPARISON OPERATORS

#EQUAL OPERATOR ---> __eq__(self, other)   