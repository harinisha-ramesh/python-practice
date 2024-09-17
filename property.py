class Circle:
    def __init__(self, radius):
        self._radius = radius  # Private attribute
        # _ denotes that the _radius is private

    @property #getter method
    def radius(self):
        """Getter method: returns the radius."""
        return self._radius

    @radius.setter
    def radius(self, value): # value parameter is the new value to set for _radius
        """Setter method: sets the radius with validation."""
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value
    
    @radius.deleter
    def radius(self):
        """Deleter method: resets the radius to a default value."""
        print("Deleting radius...")
        self._radius = 0

    @property
    def area(self):
        """Computed property: calculates the area based on the radius."""
        import math
        return math.pi * (self._radius ** 2)

    @property
    def diameter(self):
        """Computed property: calculates the diameter based on the radius."""
        return self._radius * 2

# Usage
circle = Circle(5)

print(circle.radius)   
print(circle.area)   
print(circle.diameter)

circle.radius = 10    # Calls the setter method to update the radius
print(circle.area)    # Accesses the updated area

# Deleting the radius property
del circle.radius      # Calls the deleter method to reset the radius
print(circle.radius)   # Accesses the radius after deletion, should be reset to 0
print(circle.area)     # Accesses the area after deletion, should be 0 (as radius is now 0)

try:
    circle.radius = -3  # This will raise an exception
except ValueError as e:
    print(e)
