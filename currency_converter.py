import web_utility;
import CountryList;

def convert(amount, home_currency_code, location_currency_code):
    url_string = "https://www.google.com/finance/converter?a="+str(amount)+"&from="+home_currency_code+"&to="+location_currency_code;
    print("URL STRING: " + url_string);
    result = web_utility.load_page(url_string)
    resStr = result[result.index('result'):]
    convtAmt = resStr[resStr.index("d>") + 2 :resStr.index(location_currency_code)];
    return convtAmt;

def main():
    CountryList.readFile();

    srcCtryName = input("Enter Source Country :");
    srcCtry = CountryList.getDetails(srcCtryName);
    while(srcCtry == ""):
        print("Invalid Country. Try Again");
        srcCtryName = input("Enter Source Country :");
        srcCtry = CountryList.getDetails(srcCtryName);

    destCtryName = input("Enter Destination Country :");
    destCtry = CountryList.getDetails(destCtryName);
    while(destCtry == ""):
        print("Invalid Country. Try Again");
        destCtryName = input("Enter Destination Country :");
        destCtry = CountryList.getDetails(destCtryName);

    amount = int(input("Enter Amount:"));

    print(convert(amount,srcCtry.code,destCtry.code));


main();

