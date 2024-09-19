# 1 POSITIONAL ARGUMENTS
def positional(name, age):
    print(f"Hello all, I'm {name} and I'm {age} years old")
positional("john", 24)    

# 2 KEYWORD ARGUMENTS
def keyword(color, fruit):
    print(f"I have {color} color {fruit}")
keyword(color="red", fruit='apple')    

# 3 DEFAULT ARGUMENTS
def default(mobile, price=15000):
    print(f"I have a {mobile} mobile and it's price is {price} rupees")
default('samsung')
default('vivo', 10000)

# 4 ARBITRARY ARGUMENTS
def add(*numbers):
    return sum(numbers)
print(add(1,2,3,4,5))

# 5 ARBITRARY KEYWORD ARGUMENTS
def information(**details):
    for key,value in details.items():
        print(f'{key} : {value}')
information(name="lucy", age= 20, designation= 'student')   
information(name="vivek", age= 21, designation= 'student') 

# 6 COMBINING ARGUMENTS
def combined(a,b,*num,**values):
    print(f'a: {a}, b: {b}')
    print(f'numbers: {num}')
    print(f'values: {values}')
combined('one','two',3,4,5,6,name = 'jack',age = 30)
