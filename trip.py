__author__ = 'Ashok_kumar'
import datetime

class Country:
    def __init__(self, name, code, symbol):
        self.name = name
        self.code = code
        self.symbol = symbol

    def __str__(self):
        return "("+ self.name + ", " + self.code + ", " + self.symbol + ")"

    def currency(self, amount):
        return symbol + amount

class Error(Exception):
    def __init__(self, value):
        Exception.value = value

class Details:
    locations = dict()

    def __init__(self, locations):
        self.locations = locations

    def add(self, country_name, start_date, end_date):
        try:
            datetime.datetime.strptime(start_date, '%Y/%m/%d')
            datetime.datetime.strptime(end_date, '%Y/%m/%d')
            if(start_date >= end_date):
                raise Error("Start Date should be smaller")
            for location in locations:
                date = location[1]
                if(date[0] == start_date):
                    raise Error("Start Date is already used in other Country")
            locations[country_name] = tuple(start_date, end_date)
        except:
            raise Error("Incorrect data format, should be YYYY/MM/DD")

    def is_empty(self):
        return bool(locations)

    def current_country(self, date_string):
        for location in locations:
            date = location[1]
            if(date[0] < date_string < date[1]):
                return location[0]
        return Error("Date does not match with any available date in the list")