### Assignment 6: Multiple Inheritance with Additional Attributes

#In the `Athlete` class, add an attribute `training_hours` and a method `train` that prints the training hours. Create an object of the class and call the method.

class Walker:
    def walk(self):
        print("started walking")

class Runner:
    def run(self):
        print("started runing")

class Athlete(Walker,Runner):
    def __init__(self,training_hours):
        
        self.training_hours=training_hours

    def train(self):
        print(f"Training for {self.training_hours} hours.")

athlete=Athlete(5)
athlete.run()
athlete.walk()
athlete.train()
