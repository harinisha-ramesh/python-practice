class MyContextManager:
    def __enter__(self): # Setup code
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_value, traceback): # Teardown code
        print("a" + 1)
        print("Exiting the context")
        return False  # or True if you want to suppress exceptions

with MyContextManager() as manager:
    print("Inside the context")

# exc_type ----> the type of exception
# exc_value -----> the exception object itself
# traceback -----> object that provide details about where the exception occured
