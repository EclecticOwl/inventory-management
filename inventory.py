class Inventory():


    def __init__(self):
        self.menu()

    
    def menu(self):
        print('Greetings, Human!\n')
        print('What would you like to do from the available options?\n')

        options = input(f'1) Show Available Inventory\n2) Add To Inventory\n3) Remove from inventory\n4) Exit Program\n\n>>> ')

        if options == '4':
            print()
            print('Now exiting program')
            return
    

