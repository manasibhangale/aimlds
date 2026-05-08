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
"""
## Using `super()` in Multiple Inheritance

In multiple inheritance, a child class inherits from more than one parent class.

Example:

```python id="q29g0d"
class Person:
    def __init__(self, name):
        self.name = name


class Employee:
    def __init__(self, emp_id):
        self.emp_id = emp_id


class Manager(Person, Employee):
    def __init__(self, name, emp_id):
        super().__init__(name)
        Employee.__init__(self, emp_id)


manager = Manager("Manasi", "M123")

print(manager.name, manager.emp_id)
```

### Output

```python id="lq2gvx"
Manasi M123
```

---

## Explanation

`Manager` inherits from both `Person` and `Employee`.

```python id="8x5d9l"
class Manager(Person, Employee)
```

The `super()` function calls the constructor of the next parent class according to the Method Resolution Order (MRO).

In this case, the MRO is:

```python id="o9l3rs"
Manager → Person → Employee → object
```

So:

```python id="ytpztj"
super().__init__(name)
```

calls:

```python id="3p33ds"
Person.__init__(self, name)
```

which initializes:

```python id="z5y0oh"
self.name = name
```

However, `super()` only calls the next class in the MRO and does not automatically initialize all parent classes.

Therefore, `Employee.__init__()` is called separately:

```python id="6gxrr4"
Employee.__init__(self, emp_id)
```

which initializes:

```python id="p88gmq"
self.emp_id = emp_id
```

Finally, the object contains attributes from both parent classes.

"""