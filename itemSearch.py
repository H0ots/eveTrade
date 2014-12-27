# This file contains the classes and methods involved in a user searching for a specific item's data
import csv
import requests

# gets the item name from the user
def getItem():
    item = raw_input("Enter an item name.")
    return item

# gets the system name from the user
def getSystem():
    market = raw_input("Enter trade system.")
    return market

# opens the typeids csv and finds the item id number
def openItemCSV():
    file = open('typeids.csv')
    data = csv.reader(file)
    itemID = getItem()

    for row in data:
        if itemID == row[1]:
            itemID = row[2]
            return itemID
    file.close()

# opens the solarids csv and finds the solar system id number
def openSolarCSV():
    file = open('solarids.csv')
    data = csv.reader(file)
    solarID = getSystem()

    for row in data:
        if solarID == row[1]:
            solarID = row[0]
            return solarID
    file.close()

# generates the API url used to gather our json data
def getData():
    base = "http://api.eve-central.com/api/marketstat/json"
    payload = {'typeid': openItemCSV(), 'usesystem': openSolarCSV()}
    r = requests.get(base, params=payload)
    r_data = r.json()

    min_sell = r_data[0]['sell']['min']     # gets minimum sell order data
    max_buy = r_data[0]['buy']['max']       # gets maximum buy order data
    gross_margin = min_sell - max_buy       # subtract buy and sell for profit (tax not included)
    sales_tax = min_sell * 0.009            # tax is based on Product X skills in Dodixie market
    brokers_fee = max_buy * 0.0059          # see above
    taxes = sales_tax + brokers_fee         # combines sales tax and broker's fee for total tax
    net_margin = gross_margin - taxes       # subtracts the tax from original profit
    margin_perc = (net_margin / min_sell)   # calculates "worthiness"

    # prints the relevant information
    print r.url
    print "Tax: ${:,.2f} \n".format(taxes)
    print "Minimum Sell order: ${:,.2f}".format(min_sell)
    print "Maximum Buy order: ${:,.2f}".format(max_buy)
    print "Gross Margin: ${:,.2f}".format(gross_margin)
    print "Total Profit (after taxes): ${:,.2f}".format(net_margin)
    print "Margin Percentage: {:.2%} \n".format(margin_perc)
    print "Summary:"

    if margin_perc >= .15:
        print "BUY THIS SHIT!!!"
    elif .07 <= margin_perc <= .149:
        print "Not a bad investment"
    elif .03 <= margin_perc <= .069:  # the market can swing either way, but this is generally an insignificant return
        print "Little risk, little reward."
    else:
        print "Don't bother."
    print "\n=======================================\n"

x = 0
while x == 0:
    getData()