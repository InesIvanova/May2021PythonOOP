from project.drink import Drink

class ProductRepository:
    def __init__(self,):
        self.products = []

    def add(self, product):
        self.products.append(product)

    @property
    def product_length(self):
        return len(self.products)

    def find(self, product_name):
        products_with_that_name = [product for product in self.products if product.name == product_name]
        if products_with_that_name:
            return products_with_that_name[0]

    def remove(self, product_name):
        products_with_that_name = [product for product in self.products if product.name == product_name]
        if products_with_that_name:
            self.products.remove(products_with_that_name[0])

    def __repr__(self):
        return '\n'.join([f"{product.name}: {product.quantity}" for product in self.products])


d = Drink("Cola")
d2 = Drink("water")
pr = ProductRepository()
pr.add(d)
pr.add(d2)
pr.add(d2)
print(pr.product_length)
