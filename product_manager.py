"""
product_manager.py
Clasa ProductManager - gestioneaza lista de produse disponibile.
"""


class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        """Adauga un produs in lista."""
        self.products.append(product)
        print(f"Produsul '{product.name}' a fost adaugat in inventar.")

    def display_all_products(self):
        """Afiseaza toate produsele disponibile."""
        print("\n--- PRODUSE DISPONIBILE ---")
        for product in self.products:
            product.display_info()

    def total_inventory_value(self):
        """Calculeaza valoarea totala a inventarului."""
        total = 0
        for product in self.products:
            total += product.price * product.quantity
        return total




    def remove_product(self, name):
        """Elimina un produs dupa nume."""
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                print(f"Produsul '{name}' a fost eliminat din inventar.")
                return
        print(f"Produsul '{name}' nu a fost gasit.")    



    