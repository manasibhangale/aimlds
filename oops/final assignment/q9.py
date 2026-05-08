### Assignment 9: Abstract Methods in Base Class

#Create an abstract base class named `Employee` with an abstract method `calculate_salary`. Create two derived classes `FullTimeEmployee` and `PartTimeEmployee` that implement the `calculate_salary` method. Create objects of the derived classes and call the `calculate_salary` method.
from abc import ABC,abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, salary):
        self.salary = salary

    def calculate_salary(self):
        return self.salary

class PartTimeEmployee(Employee):
    def __init__(self, hourly_rate, hours_worked):
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

# Test
full_time = FullTimeEmployee(5000)
part_time = PartTimeEmployee(20, 80)
print(full_time.calculate_salary())  # 5000
print(part_time.calculate_salary())  # 1600