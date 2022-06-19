from product import Product

from prettytable import PrettyTable

class Inventory():

    stock = []

    for i in range(10):
        sample = Product(f'Test{i}')
        sample.description = 'test description {}'.format(i)
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
        elif options == '2':
            self.add_item()
        if options == '4':
            print('\nNow exiting program')
            return
    
    def show_items(self):
        # Display items in stock

        my_table = PrettyTable()
        my_table.field_names = ['ID', 'Name', 'Description']

        for item in Inventory.stock:
            my_table.add_row((item.id, item.name, item.description))
        print(my_table)

        confirm = input('Would you like to go back to the menu?\n(Enter yes to go back to the menu.)\n')

        if confirm == 'yes' or confirm == 'y':
            self.menu()
    
    def add_item(self):

        confirm_response = 'no'
        while (confirm_response != 'yes'):
            prod_name = input('What is the name of the product?')
            prod_desc = input('Description of the product?')

            confirm_response = input(f'You entered the following entries:\nName: {prod_name}\nDescription: {prod_desc}\n\nAre these correct?\n\n>>> ')
        
        if confirm_response == 'yes':
            item_add = Product(prod_name)
            item_add.set_description(prod_desc)
            Inventory.stock.append(item_add)

            ask_again = input('Would you like to add an additional item?\n\n>>>')

            if ask_again == 'yes':
                self.add_item()
            else:
                self.menu()



            

    

