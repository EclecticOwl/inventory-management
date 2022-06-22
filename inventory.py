from product import Product
from prettytable import PrettyTable
import random

class Inventory():

    stock = []

    for i in range(1, 11):
        sample = Product(f'Test{i}')
        sample.description = 'test description {}'.format(i)
        amount = random.randint(1, 10)
        sample.quantity = amount
        stock.append(sample)

    def __init__(self):
        self.menu()

    def menu(self):
        # Options menu

        print('''
        1) Show Available Stock
        2) Add To Stock
        3) Remove From Stock
        4) Search Stock
        5) Exit Program
            ''')

        options = input('What would you like to do from the available options?\n\n>>> ')
        if options == '1':
            self.show_items()
        elif options == '2':
            self.add_item()
        elif options == '3':
            self.delete_item()
        elif options == '4':
            self.search_item()
        elif options == '5':
            print('\nNow exiting program')
            return
    
    def show_items(self):
        # Display items in stock

        my_table = PrettyTable()
        my_table.field_names = ['ID', 'Name', 'Description', 'Quantity']

        for item in Inventory.stock:
            my_table.add_row((item.id, item.name, item.description, item.quantity))
        print(my_table)

        confirm = input('Would you like to go back to the menu?\n(Enter yes to go back to the menu.)\n')

        if confirm == 'yes' or confirm == 'y':
            self.menu()
    
    def add_item(self):
        # Add an item to the inventory

        confirm_response = ''
        while (confirm_response != 'yes'):
            prod_name = input('What is the name of the product?\n\n>>> ')
            prod_desc = input('Description of the product?\n\n>>> ')
            confirm_response = input(f'You entered the following entries:\nName: {prod_name}\nDescription: {prod_desc}\n\nAre these correct?\n\n>>> ')
        
        if confirm_response == 'yes':
            item_add = Product(prod_name)
            item_add.set_description(prod_desc)
            Inventory.stock.append(item_add)

            ask_again = input('Would you like to add an additional item?\n\n>>> ')

            if ask_again == 'yes':
                self.add_item()
            else:
                self.menu()
    
    def delete_item(self):
        # Delete an item from the inventory

        my_table = PrettyTable()
        my_table.field_names = ['ID', 'Name', 'Description', 'Quantity']

        for item in Inventory.stock:
            my_table.add_row((item.id, item.name, item.description, item.quantity))
        print(my_table)
        
        confirm_response = ''
        while (confirm_response != 'yes'):
            item_to_delete = input('Please enter the ID of the item you wish to delete\n\n>>> ')
            item_index = int(item_to_delete) - 1
            item_selected = Inventory.stock[item_index]
            print(f'Confirming that you wish to delete {item_selected} from the inventory?')
            confirm_response = input('Is this correct?\n\n>>> ')

        if confirm_response == 'yes':
            Inventory.stock.pop(item_index)
            ask_again = input('Would you like to remove an additional item?\n\n>>> ')

            if ask_again == 'yes':
                self.delete_item()
            else:
                self.menu()
            
    def search_item(self):

        query = input('Please enter the item name that you wish to search for below:\n\n>>> ')
 

        for item in Inventory.stock:
            if query in item.name:
                print(f'Item name:  {item.name}\n')
                print(f'Item description: {item.description}\n')
                print(f'Item quantity: {item.quantity}\n\n')
                print('\n-----------------------\n')
        
        confirm = input('Would you like to go back to the menu?\n(Enter yes to go back to the menu.)\n')

        if confirm == 'yes' or confirm == 'y':
            self.menu()
        
        





            

    

