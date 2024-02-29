class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance.")


account = BankAccount("123456", 1000)
print("Initial balance:", account.balance)
account.deposit(500)
print("After deposit:", account.balance)
account.withdraw(200)
print("After withdrawal:", account.balance)
