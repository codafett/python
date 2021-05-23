class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance


b = BankAccount("Joe")
print(b.owner)
print(b.balance)
print(b.deposit(20))
print(b.withdraw(10))
print(b.balance)