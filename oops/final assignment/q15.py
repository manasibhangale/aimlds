### Assignment 15: Abstract Methods and Multiple Inheritance

#Create an abstract base class named `Worker` with an abstract method `work`. Create two derived classes `Engineer` and `Doctor` that implement the `work` method. Create another derived class `Scientist` that inherits from both `Engineer` and `Doctor`. Create an object of the `Scientist` class and call the `work` method.
from abc import ABC,abstractmethod
class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

class Engineer(Worker):
    def work(self):
        print("Engineer working...")

class Doctor(Worker):
    def work(self):
        print("Doctor working...")

class Scientist(Engineer, Doctor):
    def work(self):
        Engineer.work(self)
        Doctor.work(self)

# Test
scientist = Scientist()
scientist.work()