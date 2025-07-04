# account
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

    def TranferForward(self, other, amount):
        self.balance =- amount
        other.balance =+ amount

        print("tranfer complete")
        print(f'{self.balance} ${amount}.balance now ${self.balance}')
        print(f'{other.balance} ${amount}. balnce now ${other.balance}')


    
    def TranferBack(self, other, amount):
        self.balance =+ amount
        other.balance =- amount

class saving(account):
    def setInterest(self, x):
        self.interest = 0
    

