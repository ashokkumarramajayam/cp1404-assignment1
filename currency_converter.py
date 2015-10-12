import web_utility
from trip import Country

cList = []

def convert(amount, home_currency_code, location_currency_code):
    url_string = "https://www.google.com/finance/converter?a="+str(amount)+"&from="+home_currency_code+"&to="+location_currency_code
    result = web_utility.load_page(url_string)
    resStr = result[result.index('result'):]
    convtAmt = resStr[resStr.index("d>") + 2 :resStr.index(location_currency_code)]
    return float(convtAmt)


def readFile():
    file = open("currency_details.txt" ,encoding="utf8")
    for line in file:
        data = line.split(",")
        c = Country(data[0], data[1], data[2].replace("\n",""))
        cList.append(c)
    file.close()

def getDetails(countryName):
    for country in cList:
        if(country.name==countryName):
            return country
    return ""

def main():

    readFile()

    sourceCoutryName = input("Enter Home Country :")
    sourceCountry = getDetails(sourceCoutryName)
    if(sourceCountry == ""):
        print("{:>10} {:>5} {:5}".format("Invalid Details ", sourceCoutryName, tuple()))
    else:
        print("{:>10} {:>5} {:5}".format("Valid Details ", sourceCoutryName, sourceCountry))

    destinationCountryName = input("Enter Trip Country :")
    destinationCountry = getDetails(destinationCountryName)
    if(destinationCountry == ""):
        print("{:>10} {:>5} {:5}".format("Invalid Details ", destinationCountryName, tuple()))
    else:
        print("{:>10} {:>5} {:5}".format("Valid Details ", destinationCountryName, destinationCountry))


    amount = int(input("Enter Amount:"))
    if(sourceCountry == "" or destinationCountry == "" or sourceCountry.code == destinationCountry.code):
        print("{:>10} {:>10} {:>10}->{:>2} {:>10} ".format("Invalid Conversion", float(amount),sourceCoutryName, destinationCountryName,"-1.00"))
    else:
        conversion = convert(amount, sourceCountry.code,destinationCountry.code)
        reverseConversion = convert(conversion, destinationCountry.code, sourceCountry.code)
        print("{:>10} {:10.2f} {:>10}->{:>2} {:10.2f} ".format("Valid Conversion  ", float(amount),sourceCountry.code, destinationCountry.code,conversion))
        print("{:>10} {:10.2f} {:>10}->{:>2} {:10.2f} ".format("Reverse Conversion", conversion, destinationCountry.code, sourceCountry.code, reverseConversion))


main()

