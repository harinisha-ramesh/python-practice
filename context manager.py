class MyContextManager:
    def __enter__(self): # Setup code
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_value, traceback): # Teardown code
        print("Exiting the context")
        return False  # or True if you want to suppress exceptions

with MyContextManager() as manager:
    print("Inside the context")

# exc_type ----> the type of exception
# exc_value -----> the exception object itself
# traceback -----> object that provide details about where the exception occured


#USING CONTEXTLIB
from contextlib import contextmanager

@contextmanager #this decorator will simplify the creation of context managers
def context_manager():
    print("This is entering")
    try:  #contains the code that should run within the context
        yield #allows the code within the with block to run
    finally:
        print("This is exit")
with context_manager():
    print("This is inside")  
