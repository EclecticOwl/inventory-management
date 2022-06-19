from product import Product

from prettytable import PrettyTable

class Inventory():

    stock = []

    for i in range(10):
        sample = Product(f'Test{i}')
        stock.append(sample)

    def __init__(self):
        self.menu()

    def menu(self):
        # Options menu

        print('Greetings, Human!\n')
        print('What would you like to do from the available options?\n')

        options = input(f'1) Show Available Inventory\n2) Add To Inventory\n3) Remove from inventory\n4) Exit Program\n\n>>> ')
        if options == '1':
            self.show_items()
        if options == '4':
            print('\nNow exiting program')
            return
    
    def show_items(self):
        # Display items in stock

        my_table = PrettyTable()
        my_table.field_names = ['ID', 'Name']

        for item in Inventory.stock:
            my_table.add_row((item.id, item.name))
        print(my_table)

        confirm = input('Would you like to go back to the menu?\n(Enter yes to go back to the menu.)\n')

        if confirm == 'yes' or confirm == 'y':
            self.menu()

    

