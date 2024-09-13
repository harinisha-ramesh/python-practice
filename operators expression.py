#ARITHMETIC OPERATORS
x= 6
y= 4
#addition
print(x+y)
#subration 
print(x-y)
#multiplication
print(x*y)
#division
print(x/y)
#modulus 
print(x%y) # will show the remainder
#exponentiation
print(x**y) # it is meant by 6*6*6*6
#floor division
print(x//y) # will round off the value and give

#ASSIGNMENT OPERATORS
a=9
b=8
a+=b # equal to a= a+b
print(a)

a=9
b=8
a-=b # a=a-b
print(a)

a=9
b=8
a*=b # a=a*b
print(a)

a=9
b=8
a/=b #a=a/b
print(a)

a=9
b=8
a%=b #a=a%b
print(a)

#using AND
a=9
b=8
a&=b 
print(a) # now the binary bit for each digit will be done and operation

#using OR
a=9
b=8
a|=b
print(a)

#using NOT
a=9
b=8
a^=b
print(a)

#rightshift operator
a=9
b=8
a>>=b
print(a)

#leftshift operator
a=9
b=8
a<<=b
print(a)

#COMPARISON OPERATOR
#equal
x = 5
y = 3
print(x == y)

#not equal
x = 5
y = 3
print(x != y)

#Greater than
x = 5
y = 3
print(x > y)

#Less than
x = 5
y = 3
print(x < y)

#Greater than or equal to
x = 5
y = 3
print(x >= y)

#Less than or equal to
x = 5
y = 3
print(x <= y)

#LOGICAL OPERATORS
#and
x = 6
print(x > 5 and x < 10) #true statement
x = 6
print(x > 7 and x < 4) #false statement
#or
x = 5
print(x > 3 or x < 4) #true statement
x = 5
print(x > 8 or x < 4) #false statement

#IDENTITY OPERATORS
#is
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x                   #will return true if both the variables are same object
print(x is z)
print(x is y)
print(x == y)

#is not
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x                  #Returns True if both variables are not the same object
print(x is not z)
print(x is not y)
print(x != y)

#MEMBERSHIP OPERATORS
#in 
x = ["apple", "banana"]
print("banana" in x)    #Returns True if a sequence with the specified value is present in the object

#not in
x = ["apple", "banana"]
print("pineapple" not in x)  #Returns True if a sequence with the specified value is not present in the object