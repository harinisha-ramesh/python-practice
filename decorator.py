# allows or modify the behaviour of function or methods without changing the actual code

#EXAMPLE
def decorator(fun):
    def wrap():
        print("before the function is called")
        fun()
        print("After the function is called")
    return wrap    

@decorator
def new_decorator():
    print("decorator created")

new_decorator()  


#EXAMPLE ---> DECORATOR WITH ARGUMENTS
def repeat(times):
    def dec(func): #decorator function
        def wrapper(*args,**kwargs): #this function wraps the original function
            for _ in range(times):
                func(*args,**kwargs)
        return wrapper
    return dec
@repeat(times=3)
def name(name):
    print(f"Hello {name}")

name("john")    


#EXAMPLE ----> DECORATOR WITH RETURN VALUES
def new_decorator(function):
    def new_wrap(*args,**kwargs):
        result = function(*args,**kwargs)
        return result.upper()
    return new_wrap
@new_decorator
def greet(name):
    return f"Hello,my name is {name}"
print(greet('jack'))            