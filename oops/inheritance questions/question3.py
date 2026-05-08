### Assignment 3: Single Inheritance with Additional Methods

#In the `Dog` class, add a method named `bark` that prints a barking sound. Create an object of the class and call the method.


class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species

class Dog(Animal):
    def __init__(self,name,species,breed):
        super().__init__(name,species)
        self.breed=breed
    def bark(self):
        print("woof")

dog=Dog("joey","species1","golden retriever")
print(dog.name, dog.species, dog.breed)
dog.bark()