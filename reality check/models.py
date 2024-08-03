# models.py

# For now, we are using simple dictionaries. If needed, we can define classes for Person and Transaction here.

class Person:
    def __init__(self, name):
        self.name = name
        self.transactions = []

class Transaction:
    def __init__(self, amount, datetime, method, cheque=None):
        self.amount = amount
        self.datetime = datetime
        self.method = method
        self.cheque = cheque
