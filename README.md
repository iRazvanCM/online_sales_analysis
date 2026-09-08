# Online Sales Analysis

Proiect Python pentru gestionarea produselor si a cosului de cumparaturi
intr-un magazin online, dezvoltat folosind programare orientata pe obiecte (OOP)
si controlul versiunilor cu Git si GitHub.

## Structura proiectului

| Fisier | Descriere |
|--------|-----------|
| `product.py` | Clasa `Product` - modeleaza un produs |
| `product_manager.py` | Clasa `ProductManager` - gestioneaza inventarul |
| `cart.py` | Clasa `Cart` - gestioneaza cosul clientului |
| `main.py` | Programul principal |
| `.gitignore` | Fisiere excluse din versionare |

## Clase si functionalitati

### Product
- **Atribute:** `name`, `price`, `quantity`
- **Metode:**
  - `display_info()` - afiseaza informatiile despre produs
  - `update_quantity(new_quantity)` - actualizeaza cantitatea

### ProductManager
- **Atribute:** `products` (lista de produse)
- **Metode:**
  - `add_product(product)` - adauga un produs in inventar
  - `display_all_products()` - afiseaza toate produsele
  - `total_inventory_value()` - calculeaza valoarea totala a inventarului
  - `remove_product(name)` - elimina un produs dupa nume

### Cart
- **Atribute:** `cart_items` (lista de produse din cos)
- **Metode:**
  - `add_to_cart(product)` - adauga un produs in cos
  - `total_price()` - calculeaza suma totala de plata
  - `display_cart()` - afiseaza continutul cosului

## Rulare

python main.py

## Securitate

Fisierul `config.json` (care contine chei API si date confidentiale) si toate
capturile de ecran sunt excluse din versionare prin `.gitignore`.

## Autor

Razvan Muntean - https://github.com/iRazvanCM