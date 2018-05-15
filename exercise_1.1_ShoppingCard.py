from exercise_1_Product import Product


class ShoppingCart:
    def __init__(self):
        self.products = {}

    def __str__(self):
        desc = 'Zawartość koszyka:\n'
        for k, v in self.products.items():
            desc += '%s %s\n' % (k, v)
        return desc

    def add_product(self, new_product):
        self.products[new_product.id_get] = new_product

    def remove_product(self, product_id):
        print(self.products[product_id])
        del self.products[product_id]

    def change_product_quantity(self, product_id, new_quantity):
        print(self.products[product_id].quantity)
        self.products[product_id].quantity = new_quantity
        print(self.products[product_id].quantity)

    def print_receipt(self):
        for p in self.products.values():
            print("{} - {} - {}".format(p.id_get, p.name, p.get_total_sum()))

        print(sum([p.get_total_sum() for p in self.products.values()]))


sc = ShoppingCart()  # Koszyk sklepowy na początku jest pusty


p1 = Product('kot', 'rudy i wredny', 200.00, 1)  # Tworzymy nowy produkt
p2 = Product('pies', 'czarny i niezdarny', 100.00, 3)  # Tworzymy nowy produkt
p3 = Product('mangusta', 'tłusta', 1000.00, 5)  # Tworzymy nowy produkt
sc.add_product(p1)  # Dodajemy 2 koty do koszyka
sc.add_product(p2)  # Dodajemy 2 koty do koszyka
sc.add_product(p3)  # Dodajemy 2 koty do koszyka

print('-'*40)

print('sc1')
for k, v in sc.products.items():
    print('klucz: %d, obiekt: %s' % (k, v))

print('-----------')
sc.print_receipt()

print('-'*40)
sc.remove_product(2)
print('-'*40)
sc.change_product_quantity(3, 2)
print('-'*40)
sc.print_receipt()