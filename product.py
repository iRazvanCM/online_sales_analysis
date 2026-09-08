"""
product.py
Clasa Product - modeleaza un produs din magazinul online.
"""


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        """Afiseaza informatiile despre produs."""
        print(f"{self.name} | Pret: {self.price} lei | Cantitate: {self.quantity} buc")

    def update_quantity(self, new_quantity):
        """Actualizeaza cantitatea produsului."""
        self.quantity = new_quantity
        print(f"Cantitatea pentru '{self.name}' a fost actualizata la {self.quantity} buc.")