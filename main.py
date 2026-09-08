"""
main.py
Programul principal - demonstreaza gestionarea produselor si a cosului.
"""

from product import Product
from product_manager import ProductManager
from cart import Cart


manager = ProductManager()

manager.add_product(Product("Laptop", 3500.0, 10))
manager.add_product(Product("Mouse", 80.0, 50))
manager.add_product(Product("Keyboard", 250.0, 30))
manager.add_product(Product("Monitor", 1200.0, 15))
manager.add_product(Product("USB cable", 25.0, 100))

manager.display_all_products()

print(f"\nValoarea totala a inventarului: {manager.total_inventory_value()} lei")

cart = Cart()

cart.add_to_cart(manager.products[0])
cart.add_to_cart(manager.products[1])
cart.add_to_cart(manager.products[3])

cart.display_cart()

print(f"\nTotal de plata: {cart.total_price()} lei")