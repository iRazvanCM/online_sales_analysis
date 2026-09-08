"""
cart.py
Clasa Cart - gestioneaza cosul de cumparaturi al clientului.
"""


class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product):
        """Adauga un produs in cos."""
        self.cart_items.append(product)
        print(f"'{product.name}' a fost adaugat in cos.")

    def total_price(self):
        """Calculeaza suma totala de plata."""
        total = 0
        for product in self.cart_items:
            total += product.price
        return total

    def display_cart(self):
        """Afiseaza continutul cosului."""
        print("\n--- CONTINUT COS ---")
        for product in self.cart_items:
            print(f"{product.name} - {product.price} lei")