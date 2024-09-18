# child class inherits the attributes and methods of parent class is inheritance

#parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return "sound"  

#child class
class Dog(Animal):  
    def sound(self):
        return "barks"

#child class
class Cat(Animal):
    def sound(self):
        return "meow"   

#creating objects
dog = Dog("jack")
cat = Cat("tommy")

print(dog.sound())
print(cat.sound())


#EXAMPLE2
class Shape:
    def __init__(self, color):
        self.color = color
    def draw(self):
        return f"Drawing a {self.color} shape"

class Circle(Shape):
    def __init__(self, color, radius):
        self.radius = radius        
        super().__init__(color)
    def draw(self):
        return f"Drawing a {self.color} circle with radius {self.radius}"
    def area(self):
        import math
        return math.pi * (self.radius ** 2)    
    
class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)  
        self.width = width
        self.height = height
    def draw(self):
        return f"Drawing a {self.color} rectangle with width {self.width} and height {self.height}"
    def area(self):
        return self.width * self.height   

circle = Circle("Blue",4)
rectangle = Rectangle("Red", 4, 6)     

print(circle.draw())
print(rectangle.draw())

print(f"Area of Circle: {circle.area()}")
print(f"Area of Rectangle: {rectangle.area()}")
