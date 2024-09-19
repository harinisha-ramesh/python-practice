# allows or modify the behaviour of function or methods without changing the actual code

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

# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!")

# say_hello()
