from account import account
# testing
accountList = []
accountCounter = 1

#bubble sort 
def swap(first, second):
    pass

def sort():
    print("sort")

#find account
def searchList(accountList, name):
    index = -1
    for i in range(len(accountList)):
        print("searching...")
        if(accountList[i].get_name() == name):
            index = i

    return index

#one account
myAccount = account(101,"name")

#one account added to the list
accountList.append(account(accountCounter,"Jane"))
## fortesting, there is a itntial depostit in 
account[0].deposit(50)

amount = int(input("Enter a amount to deposit: "))

myAccount.deposit(amount)

#checking
myAccount.print_balance()

#checking
accountList[0].print_balance()

amount = int(input("Enter a amount to wirthdraw: "))
myAccount.withdraw(amount)
myAccount.print_balance()