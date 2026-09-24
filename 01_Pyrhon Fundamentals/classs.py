class Atm:
    
    #constructor is a special Function. it has a super power that for the execute inside the constuctor code you don't have to call it.
    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.menu()
        
    def menu(self):
        user_input = input("""
                 Hi how can i help you!
                 1. Press 1 to create a pin.
                 2. Press 2 to change a pin.
                 3. Press 3 to check Balance.
                 4. Press 4 to withdrawl Balance.
                 Anything else to exit.
                 """)
        
obj = Atm()

