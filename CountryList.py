__author__ = 'Ashok_kumar'

from Country import Country

cList = [];

def readFile():
    file = open("currency_details.txt" ,encoding="utf8");
    for line in file:
        print(line)
        data = line.split(",");
        c = Country(data[0], data[1], data[2])
        cList.append(c);
    file.close();

def getDetails(countryName):
    for country in cList:
        if(country.name==countryName):
            return country;
    return "";