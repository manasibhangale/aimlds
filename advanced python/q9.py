### Assignment 9: Class Decorator

#Create a class decorator named `singleton` that ensures a class has only one instance. Apply this decorator to a class named `DatabaseConnection` and test it.
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class DatabaseConnection:
    def __init__(self):
        print("Database connection created")

# Test
db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(db1 is db2)  # True