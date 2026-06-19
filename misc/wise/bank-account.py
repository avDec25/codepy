from decimal import Decimal
from threading import RLock


def transfer(source: BankAccount, destination: BankAccount, amount: Decimal):
    if amount <= 0:
        raise Exception("Error: Invalid amount requested to transfer")

    if source.account_id == destination.account_id:
        raise Exception("Error: Invalid request src and dest accounts are same")

    if source and destination:
        first_lock, second_lock = (source, destination) if source.account_id < destination.account_id \
            else (destination, source)

        with first_lock.lock:
            with second_lock.lock:
                source.withdraw(amount)
                destination.deposit(amount)

    print("Success: Transfer Done")


class BankAccount:
    def __init__(self, account_id: int, initial_balance=Decimal("0.0")):
        self.account_id = account_id
        self.balance = initial_balance
        self.lock = RLock()

    def deposit(self, amount: Decimal):
        with self.lock:
            self.balance += amount

    def withdraw(self, amount: Decimal):
        with self.lock:
            if self.balance < amount:
                raise Exception("Error: Insufficient Funds")
            self.balance -= amount
