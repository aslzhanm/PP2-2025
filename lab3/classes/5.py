class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner  
        self.balance = balance 
    
    def deposit(self, amount):
        self.balance += amount  
        print(f"{amount}$ deposited. New balance: {self.balance}$")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Error! Insufficient funds.")
        else:
            self.balance -= amount  
            print(f"{amount}$ withdrawn. Remaining balance: {self.balance}$")


acc = Account("John", 5000)  
acc.deposit(2000)  
acc.withdraw(3000) 
acc.withdraw(5000)  
