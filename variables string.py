#input 
name = input("Enter your name:")
print(name)
age = input(4)
print(age)

#VARIABLES
x=5
y="hello"
print(x)
print(y)

#Variables with same value
a=5
a="bye"
print(a)

#Casting in variable
value1 = float(5)
value2 = str(0.5)
value3 = int(5)
print(value1)
print(value2)
print(value3)

#Getting type
fine = type(value2)
print(fine)

#Python is case sensitive
#For multi words Variables name use- camelCase,PascalCase,snake_case
#camelcase-Each word, except the first, starts with a capital letter
firstName = "nisha"
#PascalCase-Each word starts with a capital letter
LastName = "hari"
#sanke case - Each word is separated by an underscore character
full_name = "harinisha"

#Multiple values
b, c, d = "apple" ,"orange", "grapes"
print(b)
print(c)
print(d)

#one value to multiple variables
h = r = s = "chips"
print(h)
print(r)
print(s)

#unpacking the collection
colors = ["red", "black", "white"]
color1 ,color2 , color3 = colors
print(color1)
print(color2)
print(color3)

# multiple variables - Also we can use + operator
val1 = "Python"
val2 = "is a"
val3 = "Language"
print(val1,val2,val3)

#STRINGS
#check string
hello = "This is very irritating"
print("very" in hello)

#finding length
length = "Hello Worl!"
print(len(length))

#strings are arrays
array = "Bye bye, friend"
print(array[5])

#not keyword
point = "This is not an animal"
print("vivek" not in point)
print("animal" in point)
print("an" not in point)

#SLICING
example = "We all have the Problem of Overthinking"
print(example[3:8])
#slice from the start
print(example[:6])
#slice to the end
print(example[3:])
#Negative indexing-calculating the index from the last
print(example[-6:-2])

#MODIFY STRINGS
#upper case
print(example.upper())

#lower case
print(example.lower())

#Removes white spaces
# strip() --> removes whitespace from the beginning and at the end
# but it won't remove the space in between
word = "    Byee        Byeee   "
print(word.strip())

#Replace string --> replaces a string with another string
print(example.replace("W","H"))

#split string
split = "Hello , World!"
print(split.split("o"))
print(split.split(","))

# F-STRINGS OR FORMAT() STRING
# used to join string and integer
age = 21
intro = f"My name is Harinisha,My age is {age}"
print(intro)
#modifier
check =  f"My name is Harinisha,My age is {age:.3f}"
print(check)


#ESCAPE CHARACTERS
escape = "This is so called\n \"brand\" shop"
print(escape) # \n is used for writing it in new line

