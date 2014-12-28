# This file's purpose is to calculate the top 25 item margins for a given trade system
import csv
import requests

def getSystem():
    market = raw_input("Enter a trade system: Amarr, Dodixie, Jita, or Rens\n")

    if market == 'Amarr':
        marketID = '30002187'
    elif market == 'Dodixie':
        marketID = '30002659'
    elif market == 'Jita':
        marketID = '30000142'
    elif market == 'Rens':
        marketID = '30002510'

    print marketID
    return marketID

'''
Build a function that gets the type ID for every fucking item, gathers the api data, then prints the
top 25 margins.  I am limiting this function to the top 4 trade hubs listed above.  I suppose the
data needs to be stored in an array, compared, and then printed.
1. iterate through the csv for typeID's
2. put these in URLS for data retrieval
3. store this data into an array?
4. sort items by margin percentage - greatest to least
5. print top 25 items - "Item Name" , "Margin Percent"

This is the ultimate goal and purpose of the program.
'''

getSystem()

