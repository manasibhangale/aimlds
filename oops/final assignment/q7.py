### Assignment 7: Combining Encapsulation and Inheritance

#Create a base class named `Person` with private attributes `name` and `age`. Add methods to get and set these attributes. Create a derived class named `Student` that adds an attribute `student_id`. Create an object of the `Student` class and test the encapsulation.

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

# Test
student = Student('John', 20, 'S123')
print(student.get_name(), student.get_age(), student.student_id)
student.set_name('Alice')
student.set_age(22)
print(student.get_name(), student.get_age(), student.student_id)