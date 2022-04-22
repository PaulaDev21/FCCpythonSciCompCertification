from copy import copy
from hashlib import new
from math import trunc, floor
import numpy as np

class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        to_print = self.print_title()+'\n'
        to_print += self.print_entries()
        to_print += f"Total: {self.get_balance():.2f}"

        return to_print

    def print_title(self):
        PRINT_WIDTH = 30
        toPrint = ''

        num_asterics = PRINT_WIDTH - len(self.name)
        num_asterics = trunc(num_asterics/2)+1

        for i in range(1, num_asterics):
            toPrint += '*'

        rightPrint = copy(toPrint)
        toPrint += self.name + rightPrint
        if len(toPrint) < PRINT_WIDTH:
            toPrint += '*'

        return toPrint

    def print_entries(self):
        DESCRIPTION_WIDTH = 23
        VALUE_WIDTH = 7

        entries_str = ''
        for entry in self.ledger:
            desc_str = entry["description"]
            if len(desc_str) > DESCRIPTION_WIDTH:
                desc_str = desc_str[0:23]
            else:
                while len(desc_str) < DESCRIPTION_WIDTH:
                    desc_str += ' '

            amount_str = f'{entry["amount"]:.2f}'

            while len(amount_str) < VALUE_WIDTH:
                amount_str = ' ' + amount_str

            entries_str += desc_str + amount_str + '\n'

        return entries_str

    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        sum = 0
        for op in self.ledger:
            sum += op["amount"]
        sum = float(f"{sum:.2f}")
        return sum

    def get_name(self):
        return self.name

    def transfer(self, amount, destCategory):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {destCategory.get_name()}")
            destCategory.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        if self.get_balance() < amount:
            return False
        return True

    def get_withdraws(self):
        sum = 0
        for entry in self.ledger:
            if entry["amount"] < 0:
                sum -= entry["amount"]
        return sum

cat = Category('fun')
cat.deposit(1000, "allowance for fun")
print(cat)