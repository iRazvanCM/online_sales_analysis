"""
main.py
Programul principal - demonstreaza gestionarea produselor.
"""

from product import Product
from product_manager import ProductManager


manager = ProductManager()

manager.add_product(Product("Laptop", 3500.0, 10))
manager.add_product(Product("Mouse", 80.0, 50))
manager.add_product(Product("Keyboard", 250.0, 30))
manager.add_product(Product("Monitor", 1200.0, 15))
manager.add_product(Product("USB cable", 25.0, 100))

manager.display_all_products()

print(f"\nValoarea totala a inventarului: {manager.total_inventory_value()} lei")