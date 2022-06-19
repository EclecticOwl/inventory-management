class Product:

    id = 1

    def __init__(self, name):
        self.name = name
        self.descripion = ''
        self.id = Product.id
        Product.id += 1

    def name(self):
        return self.name
    
    def __repr__(self):
        return self.name