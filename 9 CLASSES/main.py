# A simple ATM machine logic in python 

class Atm:
    
    
    def __init__(self):      # Constructor - automatically execute when obj of  a class created
        
        self.pin = ''
        self.balance = 0
        
        self.menu()
        # print("hello")
    
    def menu(self):
        '''This method will take use input'''
        
        use_input = input(
        """
        Hello, how would you like to proceed?
        1. Enter 1 to create pin
        2. Enter 2 to deposite
        3. Enter 3 to withdraw
        4. Enter 4 to check balance
        5. Enter 5 to exit                  
        """
        )
        if use_input == '1':
            self.create_pin()
        elif use_input == '2':
            self.deposite()
        elif use_input == '3':
            self.withdraw()
        elif use_input == '4':
            self.check_balance()
        else:
            print("Exit")
            
    def create_pin(self):
        ''' This method will set a pin for user.'''
        
        self.pin = input("Enter your pin: ")
        print("Pin set successfully")
            
        self.menu()
            
    def deposite(self):
        ''' This method allows a users to deposite money in their account.'''
        
        temp = input("Enter your pin: ")
        if temp == self.pin:
            amount = int(input("Enter the amount: "))
            self.balance = self.balance + amount
            print("Amount deposite successfull")
        else:
            print("Invalid pin")
                
        self.menu()
                
    def withdraw(self):
        ''' This method will allows user to withdraw from their accounts.'''
        
        temp = input("Enter your pin: ")
        if temp == self.pin:
            amount = int(input("Enter the amount: "))
            if amount < self.balance:
                self.balance = self.balance - amount
                print("Successfully withdrawel")
            else:
                print("Insufficient balance")
        else:
            print("Invalid pin")
                
        self.menu()
                
    def check_balance(self):
        ''' This method used to check balance.'''
        
        temp = input("Enter your pin: ")
        if temp == self.pin:
            print(f"Your total balance is: {self.balance}")
        else:
            print("Invalid pin")
            
        self.menu()
        
         
        
obj = Atm()