thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# Dictionary items
print(thisdict["brand"])


#DUPLICATES NOT ALLOWED ----> the last update value will get replaced
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

#Dictionary Length
print(len(thisdict))

#Data types ----> it will accept all types of data type
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)

#type
print(type(thisdict))

#dict() Constructor -----> to create a dictionary
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)


#ACCESS DICTIONARY ITEMS

#access list items ----> by reffering its key name inside the square brackets
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)

#get() ----> same functionality by giving key name
x = thisdict.get('year')
print(x)

#keys() -----> will return a list of all keys in the dictionary
x = thisdict.keys()
print(x)

#values() ----> this will return all the values in the dictionary
x = thisdict.values()
print(x)

#items() ----> will return all the items in the dictionary
x = thisdict.items()
print(x)

#Check if Key Exists ----> using in keyword
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
else:
  print("model not found")  


# CHANGE DICTIONARY ITEMS

#Change Values
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

#Update Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})


# ADD DICTIONARY ITEMS

#Adding Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

#update()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})


#REMOVE ITEMS

#pop()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

#popitem() -----> it will remove the last item
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()

#del() ----> removes the item with the specific key name
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

#del() ----> can delete the dictionary completely
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict


#clear() ----> empties the dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)


#LOOP DICTIONARIES

#using for loop
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)

# printing all values
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(thisdict[x])  

#values() ----> to return the values of the dictonary in loop
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
  print(x)

# keys() ----> to return the keys of the  dictionary in loop
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.keys():
  print(x)

#items() ----> to get both the keys and values through loop
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x,y in thisdict.items():
  print(x, y)


#COPY DICTIONARIES  

#copy() ----> make a copy of a dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

#dict() ----> also dict is used to copy
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)


#NESTED DICTIONARIES

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)

#Access Items in Nested Dictionaries
print(myfamily["child1"]['name'])

#loop through nested dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

for x, obj in myfamily.items():
    print(x)
    
    for y in obj:
        print(y + ':', obj[y])