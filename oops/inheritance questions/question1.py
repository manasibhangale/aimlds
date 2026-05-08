# Module: Inheritance Assignments
## Lesson: Single and Multiple Inheritance
### Assignment 1: Single Inheritance Basic

#Create a base class named `Animal` with attributes `name` and `species`. Create a derived class named `Dog` that inherits from `Animal` and adds an attribute `breed`. Create an object of the `Dog` class and print its attributes.

class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species

class Dog(Animal):
    def __init__(self,name,species,breed):
        super().__init__(name,species)
        self.breed=breed

dog=Dog("joey","species1","golden retriever")
print(dog.name, dog.species, dog.breed)