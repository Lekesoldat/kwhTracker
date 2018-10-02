import json
from prettytable import PrettyTable

# Create table and setup headers and alignment
table = PrettyTable()
table.field_names = ['DATE', 'MEASUREMENT', 'CONSUMPTION SINCE LAST ENTRY', 'CALCULATED PRICE']
table.align["MEASUREMENT"] = 'r'
table.align["CONSUMPTION SINCE LAST ENTRY"] = 'r'
table.align["CALCULATED PRICE"] = 'r'

# Electricity price Øre/kWh
EL_PRICE = 110 / 100

# Reads file and prints a PrettyTable to the terminal.
def readCSV():
    with open('./data.csv', 'r') as doc:
        for line in doc:
            # Ignores first line
            if line.startswith('#'):
                pass
                
            else:
                # Prepare line
                row = line.strip().split(',')

                # Structure the data
                date = row[0]
                measurement = row[1]
                consumption = row[2]
                price = round(float(row[3]), 2)

                # Add new row to table
                table.add_row([date, str(measurement) + " kWh", str(consumption) + " kWh", str(price) + " kr"])
    
    print(table)

def readJSON():
    with open('data.json') as json_data:
    # Load data
        return json.load(json_data)

def printData():
    # Get data
    d = readJSON()

    for i in range(len(d)):
        # Structure data
        date = d[i]['Date']
        measurement = d[i]['Measurement']
        consumption = d[i]['Consumption']
        price = d[i]['Calculated Price']

        # Add new row to table
        table.add_row([date, str(measurement) + " kWh", str(consumption) + " kWh", str(price) + " kr"])
        
    print(table)


def newEntry(date, measurement):
    # Grab existing data
    d = readJSON()

    # Calculate difference since last entry
    consumption = measurement - d[-1]['Measurement']
    
    price = round(consumption * EL_PRICE, 2)

    # To be appended to the data
    entry = {
        "Date": date,
        "Measurement": measurement,
        "Consumption": consumption,
        "Calculated Price": price
    }

    # Appends entry to data
    d.append(entry)

    # Overwrites current data with new updated data
    with open('./data.json', 'w') as json_data:
        json.dump(d, json_data, indent=4)
    
    print("Data added. Updated table: ")
    printData()


def main():
    date = input("Todays date? (DD.MM.YYYY)\n> ")
    consumption = float(input("What does the Power Meter say? (Ignore first 0)\n> "))

    newEntry(date, consumption)

# Comment switch, remove '#' on next line to toggle code block
#'''
printData()
'''
main()
#'''