#store multiple items in a single variable
#---> unordered
#----> unchangable
# ---> duplicates not allowed
#set-example
thisSet = {"apple", "banana", "cherry"}
print(thisSet)


# True == 1 and false == 0 ,so both are same
thisset = {"apple", "banana", "cherry", True, 1, 2, False, 0}
print(thisset)

#length of a set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

#type of the set
myset = {"apple", "banana", "cherry"}
print(type(myset))

#set constructor to make a set
thisset = set(("apple", "banana", "cherry")) # need to give double rounded brackets
print(thisset)

#access set items
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#checking the presence
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)  

thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset)

#ADD SET ITEMS

#add()
thisSet = {"apple", "banana", "cherry"}
thisSet.add("orange")
print(thisSet)

#update() ----> to add items from another set to current set
thisSet = {"apple", "banana", "cherry"}
newSet = {"orange","pineapple","grapes"}
thisSet.update(newSet)
print(thisSet)

#update() ---> to add set and any iterable object(tuple,dictionary,list)
thisSet = {"apple", "banana", "cherry"}
itr = ["orange","kiwi"]
thisSet.update(itr)
print(thisSet)

#REMOVE SET ITEMS

#remove()
thisSet = {"apple", "banana", "cherry"}
thisSet.remove("banana")
print(thisSet)

#discard()
thisSet = {"apple", "banana", "cherry"}
thisSet.discard("banana")
print(thisSet)

#pop()  ----->  will remove a random item 
thisSet = {"apple", "banana", "cherry"}
x = thisSet.pop()
print(x)
print(thisSet)

#clear()  ---> clear will empty the set
thisSet = {"apple", "banana", "cherry"}
thisSet.clear()
print(thisSet)

#del ---> will delete the entire set
thisSet = {"apple", "banana", "cherry"}
del thisSet
print(thisSet)
