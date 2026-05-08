### Assignment 15: Combining Single and Multiple Inheritance

#Create a base class named `Device` with an attribute `brand`. Create a derived class `Phone` that inherits from `Device` and adds an attribute `model`. Create another base class `Camera` with an attribute `resolution`. Create a derived class `Smartphone` that inherits from both `Phone` and `Camera`. Create an object of the `Smartphone` class and print its attributes.

class Device:
    def __init__(self,brand):
        self.brand=brand

class Phone(Device):
    def __init__(self,brand,model):
        super().__init__(brand)
        self.model=model

class Camera:
    def __init__(self,resolution):
        self.resolution=resolution

class SmartPhone(Phone,Camera):
    def __init__(self,brand,model,resolution):
        super().__init__(brand,model)
        Camera.__init__(self,resolution)

smartphone=SmartPhone("Apple","13 PRO","12MEGPIXEL")
print(smartphone.brand, smartphone.model, smartphone.resolution)
