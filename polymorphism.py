class Animal:
    def speak(self):
        return "Some animal sound"
    
class Cow(Animal):
    def speak(self):
        return "Maa"
    
class Cat(Animal):
    def speak(self):
        return "Meow"    
    
#function to demonstrate polymorphism
def animal_sound(animal):
    print(animal.speak())   

cow = Cow()
cat = Cat()

animal_sound(cow)
animal_sound(cat)

# here animal_sound is a common function that works with different types of Animal(Cow and Cat)
