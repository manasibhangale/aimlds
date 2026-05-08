### Assignment 2: Method Overriding in Single Inheritance

#In the `Dog` class, override the `__str__` method to return a string representation of the object. Create an object of the class and print it.
class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species

class Dog(Animal):
    def __init__(self,name,species,breed):
        super().__init__(name,species)
        self.breed=breed
    def __str__(self):
        return f"Dog(Name: {self.name}, Species: {self.species}, Breed: {self.breed})"

dog=Dog("joey","species1","golden retriever")
print(dog)