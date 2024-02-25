from account import account

myAccount = account()

amount = int(input("enter a amount to deposit: "))

myAccount.deposit(amount)


myAccount.print_balance()