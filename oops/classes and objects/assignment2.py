### Assignment 2: Methods in Class
#Add a method named `start_engine` to the `Car` class that prints a message when the engine starts. Create an object of the class and call the method.
class car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    
    def startengine(self):
        print("the engine has started.")
    

car1=car("toyota","camry",202)
print(car1.make,car1.model,car1.year)
car1.startengine()