import os

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def __init__(self):
        if not os.path.isfile(self.__file_name):
            open(self.__file_name, 'w').close()

    def get_products(self):
        with open(self.__file_name) as f:
            text = f.read()

        return text

    def save(self, prod_string):
        f = open(self.__file_name, 'a')
        f.write(prod_string + '\n')
        f.close()

    def add(self, *products):
        products_list = self.get_products()
        for product in products:
            if product.name in products_list:  # self.get_products():
                print(f'Продукт {product.name} уже есть в магазине')
                continue

            self.save(str(product))


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
