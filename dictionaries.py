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
