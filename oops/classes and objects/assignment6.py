### Assignment 6: Method Overriding

#In the `Employee` class, override the `__str__` method to return a string representation of the object. Create an object of the class and print it.

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Employee(Person):
    def __init__(self,name,age,emp_id):
        super().__init__(name,age)
        self.emp_id=emp_id
    def __str__(self):
        return f"Employee(Name: {self.name}, Age: {self.age}, Employee ID: {self.emp_id})"

employee=Employee("gargee",15,2)
print(employee)