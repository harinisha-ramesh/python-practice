# list ----> allow duplicates
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#LENGTH
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#DATA TYPES ----> list can be of any data type
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]
print(list1)
print(list2)
print(list3)
print(list4)

#type()
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#list() Constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#ACCESS ITEMS
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# negative indexing
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# Range of Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#Range of Negative Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#Check if Item Exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")


# CHANGE LIST ITEMS

# Change Item Value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#Change a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#Insert Items ----> inserting new item without replacing the existing values
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)


# ADD LIST ITEMS

#append items -----> to add the items at the end of the list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#Insert Items -----> to insert a list item in a specified index
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#Extend List ----> to append elements from another list to the current list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


# REMOVE LIST ITEMS

# remove() -----> removes the specified item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#Remove Specified Index ----> pop(), if no index specified in it it will delete the last item
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#del() ----> it removes the specified item and also deletes the list totally
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#delete completely
thislist = ["apple", "banana", "cherry"]
del thislist

#Clear the List ----> clear() will empty the list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


#LOOP LIST

#Loop Through a List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

#Loop Through the Index Numbers ----> can use the range() and len() to create a suitable iterable
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])
    
#Using a While Loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1	


#SORT LISTS ---> arranging it in order

#Sort List Alphanumerically ----> sort()
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# sort list numerically
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#Sorting it in descending order
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#Customize Sort Function
def myfunc(n):
  return abs(n - 50)  # here the difference between the number from 50

thislist = [100, 50, 65, 82, 23] #(100-50=50,50-50=0,65-50=15,82-50=32,23-50=27)
thislist.sort(key = myfunc)
print(thislist)

#Case Insensitive Sort ---> capital letters will come first then small letters
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# to sort a case-insensitive sort function we can use ---> str.lower
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#REVERSE ----> reverse() will reverses the current order
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)


#COPY LISTS

#copy()
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#list() ---> another way to copy the list
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#slice operator(:) ---> for making a copy of the list
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)


#JOIN LISTS

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

#appending ----> appending all items from list2 into list1, one by one
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)

#extend()
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)