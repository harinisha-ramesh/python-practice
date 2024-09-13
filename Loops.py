#WHILE LOOP
# the number of iterations is unknown and it is based on the condition 
# it will terminate when the condition becomes false

#example 1
i = 1
while i < 6:
  print(i)
  i += 1

#break statement --> we can stop the loop using 'break' even if the condition is true
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#continue statement --> we can stop the current iteration and continue to the next
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)  

#Else statement --> this else will run when the while condition becomeds false
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")  


#<........................................................................................................................................>

#FOR LOOP
# when the number of iterations is known 
# Terminates after iterating over all items or a specified range

#example
fruits = ["apple", "banana", "orange"]
for x in fruits:
  print(x)

#Looping Through a String
for x in "string":
  print(x)     

#break statement
fruits = ["apple", "banana", "orange"]
for x in fruits:
  print(x)
  if x == "banana":
    break  
  
#continue Statement
fruits = ["apple", "banana", "orange"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#Range function
# starts from 0 and ends before one number if 6 was range means it will run upto 0,1,2,3,4,5-totally 6 times not upto 6

#EXAMPLE 1
for x in range(6):
  print(x)  

#EXAMPLE 2
for x in range(2, 6):
  print(x)  

#EXAMPLE 3
# here thirst value is the increment parameter
for x in range(2, 30, 3):
  print(x)

#Else in For Loop
for x in range(6):
  print(x)
else:
  print("Finally finished!")  

#Nested Loop
colors = ["red", "black", "white"]
fruits = ["apple", "banana", "orange"]

for x in colors:
  for y in fruits:
    print(x, y)  

#pass Statement
for x in [0, 1, 2]:
  pass
    