### Assignment 12: Abstract Properties

#Create an abstract base class named `Appliance` with an abstract property `power`. Create two derived classes `WashingMachine` and `Refrigerator` that implement the `power` property. Create objects of the derived classes and access the `power` property.
from abc import ABC,abstractmethod
class Appliance:
    @property
    @abstractmethod
    def power(self):
        pass
class WashingMachine(Appliance):
    @property
    def power(self):
        return "300W" 
class Refrigerator(Appliance):
    @property
    def power(self):
        return "500W" 
    
r=Refrigerator()
w=WashingMachine()
print(r.power)
print(w.power)