#IF STATEMENT
a = 25
b = 75
if b > a:
  print("b is greater than a")

#ELIF STATEMENT
a = 25
b = 25
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")  

#ELSE STATEMENT
a = 75
b = 25
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")  

#NOT 
a = 25
b = 75
if not a > b:
  print("a is NOT greater than b")  

#NESTED IF
x = 25
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")  

#SHORT HAND IF
a = 25
b = 75
if a > b: print("a is greater than b")    

#SHORT HAND IF...ELSE
a = 25
b = 75
print("A") if a > b else print("B")

#AND
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
else:
  print("Failed")

#OR
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
else:
  print("Failed")  

#PASS STATEMENT
a = 65
b = 150
# it is just a placeholder when there is no condition inside the if statement it will avoid getting an error for being empty
if b > a:
  pass  