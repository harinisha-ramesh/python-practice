# FOR IMPORTING THE MODULE
# import mymodule.py
import math
print(math.factorial(5))
print(math.degrees(4))

#RENAMING A MODULE
# import mymodule as mm
import math as ma
print(ma.sqrt(9))

# IMPORTING A PARTICULAR FUNCTION FROM A MODULE
# from mymodule import function1

from math import pi
print(2 * pi)


#IMPORTING DATETIME
import datetime
print(datetime.datetime.now())

from datetime import timezone
print(timezone.max)

x = datetime.datetime.now()
print(x.strftime("%A")) #day full name
print(x.strftime("%a")) #day short name


#If I have a module and in that to access only the dictionary it can be written as follows
# A file called module1 is created
#importing this in another module

#METHOD 1
import module1 as m1
a = m1.person1['country']
print(a)

#METHOD 2
import module1 
a = module1.person1['age']
print(a)

#METHOD 3 
from module1 import person1
a = person1['name']
print(a)