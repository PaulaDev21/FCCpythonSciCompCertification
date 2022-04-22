from copy import copy
from math import trunc

class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        to_print = self.__print_title()+'\n'
        to_print += self.__print_entries()
        to_print += f"Total: {self.get_balance():.2f}"

        return to_print
    
    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_withdraws(self):
        sum = 0
        for entry in self.ledger:
            if entry["amount"] < 0:
                sum -= entry["amount"]
        return sum

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


    def __print_title(self):
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


    def __print_entries(self):  
        entries_str = ''
        for entry in self.ledger:
            desc_str = self.__get_short_description(entry["description"])
            amount_str = self.__get_amount_formated(entry["amount"])

            entries_str += desc_str + amount_str + '\n'

        return entries_str
    
    def __get_short_description(self, desc_str):
        DESCRIPTION_WIDTH = 23

        if len(desc_str) > DESCRIPTION_WIDTH:
            desc_str = desc_str[0:DESCRIPTION_WIDTH]
        else:
            while len(desc_str) < DESCRIPTION_WIDTH:
                desc_str += ' '
        return desc_str


    def __get_amount_formated(self, amount):
        VALUE_WIDTH = 7
        amount_str = f'{amount:.2f}'

        while len(amount_str) < VALUE_WIDTH:
            amount_str = ' ' + amount_str

        return amount_str

cat = Category('fun')
cat.deposit(1000, "allowance for fun")
print(cat)
