__author__ = 'Ashok_kumar'
class Country:
    def __init__(self, name, code, symbol):
        self.name = name;
        self.code = code;
        self.symbol = symbol;
    def __str__(self):
        return name + " " + code + " " + symbol;

    def currency(self, amount):
        return symbol + amount;
