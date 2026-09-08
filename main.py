"""
main.py
Programul principal - demonstreaza gestionarea produselor si a cosului.
"""

from product import Product
from product_manager import ProductManager
from cart import Cart


manager = ProductManager()

manager.add_product(Product("Gaming Laptop", 4200.0, 8))
manager.add_product(Product("Wireless Mouse", 120.0, 60))
manager.add_product(Product("Mechanical Keyboard", 380.0, 25))
manager.add_product(Product("4K Monitor", 1800.0, 12))
manager.add_product(Product("USB-C cable", 35.0, 150))

cart = Cart()

cart.add_to_cart(manager.products[0])
cart.add_to_cart(manager.products[1])
cart.add_to_cart(manager.products[3])

cart.display_cart()

print(f"\nTotal de plata: {cart.total_price()} lei")