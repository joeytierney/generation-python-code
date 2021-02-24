class Bank:
    def __init__(self):
        self.balance = 0

    def deposit(self):
        amount = float(input("Deposit amount: "))
        self.balance += amount
        print("\nAmount Deposited:",amount)

    def withdraw(self):
        amount = float(input("How much do you wish to withdraw? "))
        if self.balance >= amount:
            self.balance -= amount
            print("\nYou have withdrawn:",amount)
        else:
            print("\nInsufficient funds")

    def checkBalance(self):
        print("\nYour current balance is:",self.balance)

class Person:
    def __init__(self, name):
        self.name = name
        self.balance = 10000

print("***** WELCOME *****")
name = input("Enter your name: ")
currentUser = Person(name)
print("\n")
userBalance = Bank()

userBalance.deposit()
userBalance.withdraw()
userBalance.checkBalance()