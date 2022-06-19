from product import Product
from inventory import Inventory

stock = []

for i in range(10):
    sample = Product(f'Test{i}')
    stock.append(sample)



main_program = Inventory()
