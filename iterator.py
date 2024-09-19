#example 1
mystr = "encyclopedia"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

#Looping through an Iterator
mytuple = ("apple", "banana", "cherry")
for x in mytuple:
  print(x)
#Iterate the characters of the string
mytuple = ("Hello all")
for x in mytuple:
  print(x)

#CREATING OWN ITERATOR
class Counter:
    def __init__(self, limit):
        self.limit = limit
        self.current = 1

    def __iter__(self):  # Returns the iterator object (itself)
        return self      #means counter itself is an iterator

    def __next__(self):  # Defines how to get the next item
        if self.current > self.limit:
            raise StopIteration  # Stop when we reach the limit
        self.current += 1
        return self.current - 1
counter = Counter(3)

print(next(counter)) 
print(next(counter))  
print(next(counter))  
