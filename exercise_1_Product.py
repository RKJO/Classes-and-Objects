class Product:
    __id = None
    next_id = 1
    name = None
    description = None
    price = None
    quantity = None

    def __str__(self):
         return '%d: %s, %s, %d, %d' % (self.__id, self.name, self.description, self.price, self.quantity)

    def __init__(self, n, d, p, q):
        if isinstance(n, str) and isinstance(d, str):
            self.name = n
            self.description = d
        else:
            raise Exception("Zła nazwa lub opis")

        if isinstance(p, float) and p >= 0.01:
            self.price = p
        else:
            raise Exception('Zła cena produktu')

        if isinstance(q, int) and q >= 1:
            self.quantity = q
        else:
            raise Exception('Zła liczność produktu')

        self.__id = self.next_id
        Product.next_id += 1

    def get_total_sum(self):
        total_sum = self.quantity * self.price
        return total_sum if self.quantity < 3 else 0.8 * total_sum

    @property
    def id_get(self):
        return self.__id