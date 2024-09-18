# binding the methods and attributes within the class is encapsulation

class Person:
    def __init__(self, name, age) :
        self.name = name  #public attribute
        self.__age = age  #private attribute
    
    #using get method for private attribute
    def get_age(self):
        return self.__age    
    
    #using set method for private attribute
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive")    

    #public method
    def intro(self):
        return f"Hi my name is {self.name} and I'm {self.__age} years old"        

#creating an object
person1 = Person("John",34)
person2 = Person("Nick",25)

#Access the public attribute
print(person2.name)

#access the private attribute
print(person2.get_age())

#update the private attirbute 
person1.set_age(30)
print(person1.get_age())

#setting invalid age
person2.set_age(-3)

#access public method
print(person2.intro())
    