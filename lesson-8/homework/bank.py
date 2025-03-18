import json
import random

class Account:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        return "Insufficient funds or invalid amount."

class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_from_file()

    def create_account(self, name, initial_deposit):
        account_number = str(random.randint(10000, 99999))
        while account_number in self.accounts:
            account_number = str(random.randint(10000, 99999))
        self.accounts[account_number] = Account(account_number, name, initial_deposit)
        self.save_to_file()
        return f"Account created! Account Number: {account_number}"

    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            return f"Account {account.account_number}: {account.name}, Balance: ${account.balance}"
        return "Account not found."

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            result = account.deposit(amount)
            self.save_to_file()
            return result
        return "Account not found."

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            result = account.withdraw(amount)
            self.save_to_file()
            return result
        return "Account not found."

    def save_to_file(self):
        with open("accounts.json", "w") as f:
            json.dump({acc_num: vars(acc) for acc_num, acc in self.accounts.items()}, f)

    def load_from_file(self):
        try:
            with open("accounts.json", "r") as f:
                data = json.load(f)
                self.accounts = {acc_num: Account(**details) for acc_num, details in data.items()}
        except (FileNotFoundError, json.JSONDecodeError):
            self.accounts = {}

bank = Bank()
print(bank.create_account("Alice", 500))
print(bank.create_account("Bob", 1000))
print(bank.view_account("10001"))
print(bank.deposit("10001", 200))
print(bank.withdraw("10001", 300))

