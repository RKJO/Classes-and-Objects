class Book:
    name = None
    price = None
    author = None

    def __init__(self, n, p, a):
        print("Tworzę nową książkę")
        self.name = n
        self.price = p
        self.author = a

    def __repr__(self):
        return "{} by {} for {}".format(self.name, self.author, self.price)


class EBook(Book):
    size_in_mb = None

    def __init__(self, n, p, a, s):
        print("Tworzę nowego ebooka")
        super(EBook, self).__init__(n, p, a)
        self.size_in_mb = s


ebook1 = EBook('Hobbit', 35.95, 'J. R. R. Tolkien', 12)
print(ebook1)

