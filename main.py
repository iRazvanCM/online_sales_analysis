"""
main.py
Programul principal - demonstreaza gestionarea produselor.
"""

from product import Product
from product_manager import ProductManager


manager = ProductManager()

manager.add_product(Product("Gaming Laptop", 4200.0, 8))
manager.add_product(Product("Wireless Mouse", 120.0, 60))
manager.add_product(Product("Mechanical Keyboard", 380.0, 25))
manager.add_product(Product("4K Monitor", 1800.0, 12))
manager.add_product(Product("USB-C cable", 35.0, 150))