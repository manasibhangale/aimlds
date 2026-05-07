### Assignment 3: Class with Constructor
#Create a class named `Student` with attributes `name` and `age`. Use a constructor to initialize these attributes. Create an object of the class and print its attributes.
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
student=Student("manasi",22)
print(student.name,student.age)