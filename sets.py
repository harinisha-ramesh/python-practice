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


#LOOP ITEMS
thisSet = {"apple", "banana", "cherry"}
for x in thisSet:
  print(x)

#JOIN SETS

#union() -----> returns a new set with all items from both sets
set1 = {'a','b','c'}
set2 = {1, 2, 3, 'a'}    # will not allow duplicates
set3 = set1.union(set2)
print(set3)

# | -----> instead of union() we can use this symbol
set1 = {'a','b','c'}
set2 = {1, 2, 3, 4}
set3 = set1 | set2
print(set3)

# Join multiple sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
new_set = set1.union(set2, set3, set4)
print(new_set)

# join a set and tuple ---> the result will be tuple
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

#update() ----> insert all items from one set into another updates the original set
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3, 'b'}   # will not allow duplicates
set1.update(set2)
print(set1) 

#Intersection ---> return a new set where only duplicates are allowed
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)

# & ----> for intersectionwe can use this operator also
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)

# intersection_update() ---> keep only duplicates but will change the original set instead of creating new
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)

# Difference() and - operator ----> will return a new set it will contain the items present in set1 and that should not be present in set2
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)

# difference_update() ----> same like intersection_update will change the original set

# symmetric_difference() and ^ operator---> will keep the items that are not present in both sets
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)

# symmetric_difference_update() ----> same like intersection_update will change the original set