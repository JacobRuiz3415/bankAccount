
class account:

    def __init__(self, name):
        self.name = name
        self.balance = 0
        print("Account created")

    def get_Balance(self):
        return self.balance
    
    def print_balance(self):
        print(f"Acount name:{self.name}")
        print(f"${self.balance}")

    def withdraw(self, amount):
        self.balance =- amount

    def deposit(self, amount):
        self.balance =+ amount

    

    

