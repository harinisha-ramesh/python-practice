# belongs to class but does not operate on class or instance itself 
# does not take the instance or class as its first argument 

#syntax for static method
class MyClass:
    @staticmethod
    def my_static_method():
        print("This is a static method")

#example
class MathOperations:
    # Static method for adding two numbers
    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def multiply(x, y):
        return x * y

# Calling the static method directly from the class
print(MathOperations.add(5, 10))
print(MathOperations.multiply(7, 8))
 

# Static methods can also be called from instances, though it's less common
math_op = MathOperations()
print(math_op.add(20, 30))  
