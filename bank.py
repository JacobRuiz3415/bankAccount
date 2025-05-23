from account import account
# testing
accountList = []



accountList = [account()]
#one account
myAccount = account()

#one account added to the list
accountList.append(account())

amount = int(input("Enter a amount to deposit: "))

myAccount.deposit(amount)

myAccount.print_balance()

amount = int(input("Enter a amount to deposit: "))
myAccount.withdraw(amount)
