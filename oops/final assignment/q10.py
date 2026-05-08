### Assignment 10: Encapsulation in Data Classes

#Create a data class named `Product` with private attributes `product_id`, `name`, and `price`. Add methods to get and set these attributes. Ensure that the price cannot be set to a negative value.

class Product:
    def __init__(self, product_id, name, price):
        self.__product_id = product_id
        self.__name = name
        self.__price = price

    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def set_product_id(self, product_id):
        self.__product_id = product_id

    def set_name(self, name):
        self.__name = name

    def set_price(self, price):
        if price < 0:
            print("Price cannot be negative!")
        else:
            self.__price = price

# Test
product = Product('P001', 'Laptop', 1000)
print(product.get_product_id(), product.get_name(), product.get_price())
product.set_price(-500)  # Price cannot be negative!
product.set_price(1500)
print(product.get_product_id(), product.get_name(), product.get_price())