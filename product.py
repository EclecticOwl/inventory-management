class Product:

    id = 1

    def __init__(self, name):
        self.name = name
        self.description = ''
        self.quantity = 0
        self.id = Product.id
        Product.id += 1
    
    def __repr__(self):
        return self.name