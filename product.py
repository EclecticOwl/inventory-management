class Product:

    id = 1

    def __init__(self, name):
        self.name = name
        self.description = ''
        self.id = Product.id
        Product.id += 1

    def get_name(self):
        return self.name
    
    def set_name(self, value):
        self.name = value

    def get_description(self):
        return self.description
    
    def set_description(self, value):
        self.description = value

    def get_id(self):
        return self.id
    
    def __repr__(self):
        return self.name