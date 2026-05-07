### Assignment 7: Class Composition

#Create a class named `Address` with attributes `street`, `city`, and `zipcode`. Create a class named `Person` that has an `Address` object as an attribute. Create an object of the `Person` class and print its address.

class Address:
    def __init__(self,street,city,zipcode):
        self.street=street
        self.city=city
        self.zipcode=zipcode

class Person:
    def __init__(self , name, age, address):
        self.name=name
        self.age=age
        self.address=address

address=Address("tarapur","boisar",401501)
person = Person('manasi', 22, address)
print(person.address.street, person.address.city, person.address.zipcode)
