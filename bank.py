from account import account
# testing
accountList = []

#bubble sort 
def sort():
    print("sort")

#find account
def searchList(accountList, number):
    return

accountList = [account()]
#one account
myAccount = account("name")

#one account added to the list
accountList.append(account("Jane"))

amount = int(input("Enter a amount to deposit: "))

myAccount.deposit(amount)

#checking
myAccount.print_balance()

#checking
accountList[0].print_balance()

amount = int(input("Enter a amount to deposit: "))
myAccount.withdraw(amount)
