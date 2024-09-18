# try ---> test a block of code for errors
# except ---> handles the error 
# else ---->if no exception occurs else block will run
# finally ---> executes the code whether an exception is raised or not

# example 1
try:
    a = 5
    print(a)
except:
    print("a is not defined")
finally:
    print("file is closed")        


# example 2
try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print(f"Result: {result}")
except ValueError as ve:
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError as zde:
    print("Error: Division by zero is not allowed.")
else:
    print("Operation successful!")
finally:
    print("This will always execute, regardless of exceptions.")
    


#ERROR HANDLING

def divide_numbers(a, b):
    try:
        # Logical error check
        if b == 0:
            raise ValueError("Cannot divide by zero.")  # Raising an exception for zero division

        # Runtime error check (if non-numeric values are passed)
        result = a / b
        print(f"Result: {result}")

    except ValueError as ve:
        # Handles both our custom exception and other ValueErrors
        print(f"ValueError: {ve}")

    except TypeError as te:
        # Handles cases where inputs are not numbers (runtime error)
        print(f"TypeError: {te}")

    except Exception as e:
        # Catches any other generic exception
        print(f"Unexpected error: {e}")

    finally:
        # Cleanup or final message
        print("Operation complete.")

# Test cases for error handling
divide_numbers(10, 2)    # No error, should print the result
divide_numbers(10, 0)    # Raises ValueError for division by zero
divide_numbers("10", 2)  # Raises TypeError for invalid input type
