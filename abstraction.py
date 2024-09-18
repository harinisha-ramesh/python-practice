from abc import ABC, abstractmethod

class Appliance(ABC): #abstrat class
    @abstractmethod
    def turn_on(self): #abstract method
        pass

    def turn_off(self):
        pass

class washingMachine(Appliance):
    def turn_on(self):
        return "Washing machine is running"
    def turn_off(self):
        return "Washing machine is off now"
    
class refrigerator(Appliance):
    def turn_on(self):
        return "Refrigerator is now on"
    def turn_off(self):
        return "Refrigerator is now turned off"
    
def operating_appliance(appliance):
    print(appliance.turn_on())
    print(appliance.turn_off())

wm = washingMachine()
fridge = refrigerator()

operating_appliance(wm)
operating_appliance(fridge)