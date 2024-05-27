# Abstraction
from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def display_details(self):
        pass

# Inheritance
class Electronics(Product):
    def __init__(self, name, price, brand, model):
        super().__init__(name, price)
        self.brand = brand
        self.model = model

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Price: ${self.price}")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")

class Clothing(Product):
    def __init__(self, name, price, size, color):
        super().__init__(name, price)
        self.size = size
        self.color = color

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Price: ${self.price}")
        print(f"Size: {self.size}")
        print(f"Color: {self.color}")

# Encapsulation
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_to_cart(self, product):
        self.items.append(product)

    def remove_from_cart(self, product):
        self.items.remove(product)

    def display_cart(self):
        print("Shopping Cart:")
        for product in self.items:
            product.display_details()
            print()

# Polymorphism
if __name__ == "__main__":
    electronics = Electronics("Smartphone", 599.99, "Apple", "iPhone 13")
    clothing = Clothing("T-Shirt", 29.99, "M", "Blue")

    cart = ShoppingCart()
    cart.add_to_cart(electronics)
    cart.add_to_cart(clothing)

    cart.display_cart()
