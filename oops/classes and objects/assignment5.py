### Assignment 5: Class Inheritance
#Create a base class named `Person` with attributes `name` and `age`. Create a derived class named `Employee` that inherits from `Person` and adds an attribute `employee_id`. Create an object of the derived class and print its attributes.

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Employee(Person):
    def __init__(self,name,age,emp_id):
        super().__init__(name,age)
        self.emp_id=emp_id

employee=Employee("Manasi",22,1)
print(employee.name,employee.age,employee.emp_id)