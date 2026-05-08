### Assignment 9: Using `super()` in Multiple Inheritance

#Create a class named `Person` with an attribute `name`. Create a class named `Employee` with an attribute `employee_id`. Create a derived class `Manager` that inherits from both `Person` and `Employee`. Use the `super()` function to initialize the attributes. Create an object of the `Manager` class and print its attributes.

class Person:
    def __init__(self,name):
        self.name=name
class Employee:
    def __init__(self,emp_id):
        self.emp_id=emp_id
class Manager(Person,Employee):
    def __init__(self,name,emp_id):
        super().__init__(name)
        Employee.__init__(self,emp_id)

manager = Manager('Manasi', 'M123')
print(manager.name, manager.emp_id)