import json
from prettytable import PrettyTable
from constants import *
import pymongo
import os

# - - - - - - - - - - - - - - - - - - - D A T A B A S E - - - - - - - - - - - - - - - - - - -

# Require username and password to run program, quit if missing.
if not DB_USERNAME in os.environ or not DB_PASSWORD in os.environ:
    print("Missing database username and/or password.")
    exit(1)

# Connect to database with provided username and pwd
client = pymongo.MongoClient("mongodb://{}:{}@ds119993.mlab.com:19993/kwhtracker".format(
    os.environ[DB_USERNAME],
    os.environ[DB_PASSWORD]
))

# Choose database
db = client.kwhtracker

# Grab the collection
measurements = db.measurements


# - - - - - - - - - - - - - - - - - - T A B L E  S E T U P - - - - - - - - - - - - - - - - - - 

# Create table and setup headers and alignment
table = PrettyTable()
table.field_names = ['DATE', 'MEASUREMENT', 'CONSUMPTION SINCE LAST ENTRY', 'CALCULATED PRICE']
table.align["MEASUREMENT"] = 'r'
table.align["CONSUMPTION SINCE LAST ENTRY"] = 'r'
table.align["CALCULATED PRICE"] = 'r'


def printData():
    # Iterates all documents in the collection
    for m in measurements.find():
        date = m['date']
        measurement = m['measurement']
        consumption = m['consumption']
        price = m['calculatedPrice']

        # Add new row to table
        table.add_row([date, str(measurement) + " kWh", str(consumption) + " kWh", str(price) + " kr"])
        
    print(table)


def newEntry(date, measurement):
    # Grabs previous measurement, - sorted by id´s
    previous = measurements.find().limit(1).sort([('_id', pymongo.DESCENDING)]).next()

    # Calculate difference since last entry
    consumption = round(measurement - previous['measurement'], 2)
    
    price = round(consumption * EL_PRICE, 2)

    # To be appended to the data
    entry = {
        "date": date,
        "measurement": measurement,
        "consumption": consumption,
        "calculatedPrice": price
    }

    # Appends entry to data
    measurements.insert_one(entry)
    
    print("Data added. Updated table: ")
    printData()


def main():
    date = input("Todays date? (DD.MM.YYYY)\n> ")
    consumption = float(input("What does the Power Meter say? (Ignore first 0)\n> "))

    newEntry(date, consumption)

# Comment switch, remove '#' on next line to toggle code block
'''
printData()
'''
main()
#'''
