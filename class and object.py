# Define a class
class Car:
    def __init__(self, brand, model):  # Constructor method
        self.brand = brand  # Attribute 
        self.model = model  # Attribute 

    def drive(self):  # Method
        return f"{self.brand} {self.model} is driving!"

# Create objects from the class
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

# Access attributes and methods
print(car1.brand)  
print(car2.model)  
print(car1.drive())  


# class ----> car is the class
# attribute ----> brand and model are the attributes
# method ---> drive is the method
# object/instance ----> car1 and car2 are the objects