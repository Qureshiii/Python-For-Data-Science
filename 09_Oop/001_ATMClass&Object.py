class Atm:
    
    #constructor is a special Function. it has a super power that for the execute inside the constuctor code you don't have to call it.
    def __init__(self):
        self.pin =''
        self.balance = 0
        self.menu()
        
    def menu(self):
        user_input = input("""
                 Hello! how would you like to procced?
                 1. Press 1 to create pin.
                 2. Press 2 to deposit.
                 3. Press 3 to withdraw.
                 4. Press 4 to check Balance.
                 5. Press 5 to Exit.
    """)
        
        if user_input == '1':
            self.create_pin()
            self.menu()
        
        elif user_input == '2':
            self.deposit()
            self.menu()
        
        elif user_input == '3':
            self.withdraw()
            self.menu()
        
        elif user_input == '4':
            self.balance_check()
            self.menu()
        
        else:
            print('bye')
            
            

    def create_pin(self):
        self.pin = input("Enter your Pin")
        print('Pin set successfully')
        


    def deposit(self):
        temp = input("Enter your pin")

        if temp == self.pin:
            amount = int(input("Enter you amount"))
            self.balance = self.balance + amount
            print('Deposit Successful')
        else:
            print('Invalid Pin')
            
        
    def withdraw(self):
        temp = input("Enter your pin")
        
        if temp == self.pin:
            withdrawl = int(input("Enter your withdrawl amount"))
            
            if self.balance >= withdrawl:
                self.balance = self.balance - withdrawl
                print('Withdrawl Successful Current Balance is', self.balance)
            else:
                print('Insuficient Balance')
        
        else:
            print('Invalid Pin')            
                
    
    def balance_check(self):
        temp = input("Enter your pin")
        
        if temp == self.pin:
            print('Your Balance is',self.balance)
        else:
            print('Invalid Pin')
        

Abl = Atm()
Abl.balance_check()