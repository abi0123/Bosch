import datetime

class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.transactions = []  # keep track of deposits/withdrawals

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        self.transactions.append((datetime.datetime.now(), "Deposit", amount, self.balance))
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance -= amount
        self.transactions.append((datetime.datetime.now(), "Withdraw", amount, self.balance))
        print(f"✅ Withdrew {amount}. New balance: {self.balance}")

    def get_balance(self):
        return self.balance

    def print_transactions(self):
        print(f"\n📒 Transaction history for {self.account_holder}:")
        for t in self.transactions:
            time, ttype, amt, bal = t
            print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {ttype} {amt} | Balance: {bal}")

    def __str__(self):
        return f"[{self.account_number}] {self.account_holder} | Balance: {self.balance}"


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0.0, interest_rate=0.10):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        print(f"💰 Interest applied at {self.interest_rate*100}%: {interest}")


class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0.0, overdraft_limit=1000.0):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance + self.overdraft_limit:
            print("Exceeds overdraft limit.")
            return
        self.balance -= amount
        self.transactions.append((datetime.datetime.now(), "Withdraw", amount, self.balance))
        print(f"Withdrew {amount} using overdraft. New balance: {self.balance}")


class FixedDepositAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0.0, lock_in_years=1):
        super().__init__(account_number, account_holder, balance)
        self.lock_in_years = lock_in_years
        self.opened_on = datetime.datetime.now()

    def withdraw(self, amount):
        elapsed_years = (datetime.datetime.now() - self.opened_on).days / 365
        if elapsed_years < self.lock_in_years:
            print("Withdrawal not allowed. Locked for {self.lock_in_years} years.")
            return
        super().withdraw(amount)


class Bank:
    def __init__(self):
        self.accounts = {}
        self.account_counter = 1000 

    def create_account(self, account_type, account_holder, balance=0.0):
        self.account_counter += 1
        acc_num = str(self.account_counter)
        if account_type == "savings":
            acc = SavingsAccount(acc_num, account_holder, balance)
        elif account_type == "current":
            acc = CurrentAccount(acc_num, account_holder, balance)
        elif account_type == "fd":
            acc = FixedDepositAccount(acc_num, account_holder, balance)
        else:
            print("Unknown account type")
            return None
        self.accounts[acc_num] = acc
        print(f" Created {account_type} account for {account_holder} with number {acc_num}")
        return acc

    def transfer_funds(self, from_acc, to_acc, amount):
        if from_acc not in self.accounts or to_acc not in self.accounts:
            print(" not found")
            return
        sender = self.accounts[from_acc]
        receiver = self.accounts[to_acc]
        if sender.get_balance() + (sender.overdraft_limit if isinstance(sender, CurrentAccount) else 0) < amount:
            print("insufficient balance")
            return
        sender.withdraw(amount)
        receiver.deposit(amount)
        print(f"Transferred {amount} from {from_acc} to {to_acc}")
bank = Bank()

savings = bank.create_account("savings", "Abinaya", 900.0)
current = bank.create_account("current", "ABINAV", 300.0)
fd = bank.create_account("fd", "Bob Smith", 2000.0)

print(" Savings Account")
print(savings)
savings.deposit(300)
savings.withdraw(200)
savings.apply_interest()
savings.print_transactions()

print("Current Account")
print(current)
current.deposit(1000)
current.withdraw(1800) 
current.print_transactions()

print("Fixed Deposit")
print(fd)
fd.withdraw(500) 
fd.print_transactions()

print("Fund Transfer Demo")
bank.transfer_funds(savings.account_number, current.account_number, 200)
savings.print_transactions()
current.print_transactions()

