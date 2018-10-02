import json
from prettytable import PrettyTable
# Create table and setup headers and alignment

table = PrettyTable()
table.field_names = ['DATE', 'MEASUREMENT', 'CONSUMPTION', 'CALCULATED PRICE']
table.align["MEASUREMENT"] = 'r'
table.align["CONSUMPTION"] = 'r'
table.align["CALCULATED PRICE"] = 'r'

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
        d = json.load(json_data)

        # Traverse .JSON file
        for i in range(len(d)):

            # Structure data
            date = d[i]['Date']
            measurement = d[i]['Measurement']
            consumption = d[i]['Consumption']
            price = round(float(d[i]['Calculated Price']))

            # Add new row to table
            table.add_row([date, str(measurement) + " kWh", str(consumption) + " kWh", str(price) + " kr"])
        
        print(table)

readJSON()

