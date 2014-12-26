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

    min_sell = r_data[0]['sell']['min']
    max_buy = r_data[0]['buy']['max']
    gross_margin = min_sell - max_buy
    sales_tax = min_sell * 0.009
    brokers_fee = max_buy * 0.0059
    taxes = sales_tax + brokers_fee
    net_margin = gross_margin - taxes
    margin_perc = (net_margin / min_sell)

    print
    print r.url
    print "Tax: ${:,.2f}".format(taxes)
    print
    print "Minimum Sell order: ${:,.2f}".format(min_sell)
    print "Maximum Buy order: ${:,.2f}".format(max_buy)
    print "Gross Margin: ${:,.2f}".format(gross_margin)
    print "Total Profit (after taxes): ${:,.2f}".format(net_margin)
    print "Margin Percentage: {:.2%}".format(margin_perc)
    print
    print "Summary:"

    if margin_perc >= .07:
        print "BUY THIS SHIT!!!"
    elif .03 <= margin_perc <= .069:
        print "Little risk, little reward."
    else:
        print "Don't bother."

getData()