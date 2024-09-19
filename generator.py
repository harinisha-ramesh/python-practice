#example 1
def generator():
    yield "a"
    yield 'b'
    yield 'c'
gen = generator()
for x in gen:
    print(x)    

#example for counting numbers
def count_numbers(max):
    count = 1
    while count <=max:
        yield count
        count += 1
counter = count_numbers(5)
print(next(counter))
print(next(counter))

#GENERATOR EXPRESSION 
# A generator expression that yields squares of numbers from 0 to 4
gen = (x * x for x in range(5))

# Use next() to get values one by one
print(next(gen))  
print(next(gen))  
print(next(gen))  
print(next(gen))  
print(next(gen))  

#summing numbers with generator expression
sum_squares = sum(x * x for x in range(10))
print(sum_squares)

# this parenthisis () makes the expression to work as a generator