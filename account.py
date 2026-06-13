# account
class account:

    def __init__(self, ID, name):
        self.ID = ID
        self.name = name
        self.balance = 0
        print("Account created")

    def get_Balance(self):
        return self.balance
    
    def get_ID(self):
        pass

    def get_name(self):
        return self.name
    
    def print_balance(self):
        print(f"Acount name:{self.name}")
        print(f"${self.balance}")

    def withdraw(self, amount):
        if ((self.get_Balance() - amount) < 0):
            print("there is a overdraft")
        print(f'${self.balance}before + ${amount}. account balance now ${self.balance}')
        self.balance =- amount

    def deposit(self, amount):
        print(f'${self.balance}before + ${amount}. account balance now ${self.balance}')
        self.balance =+ amount

    def Tranfer_Forward(self, other, amount):
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
        self.interest = x
    

