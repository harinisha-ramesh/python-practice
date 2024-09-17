#they are called on the class , not on instances

# defines class method using the @classmethod decorator
# should always have 'cls' as its first argument

#example
class Car:
    # Class attribute (shared across all instances)
    car_count = 0

    # __init__ is automatically called when a new object is created
    def __init__(self, model):
        self.model = model
        Car.car_count += 1  # This modifies the class attribute

    # Class method: works with the class, not instances
    @classmethod
    def total_cars(cls):
        return f"Total cars created: {cls.car_count}"

# Creating car objects (instances of the class)
car1 = Car("Sedan")
car2 = Car("SUV")

# Calling the class method directly using the class name
print(Car.total_cars())

# We can also call the class method using an instance, but it still refers to the class
print(car1.total_cars()) 



