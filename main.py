from prettytable import PrettyTable
# Create table and setup headers and alignment

table = PrettyTable()
table.field_names = ['DATE', 'MEASUREMENT', 'CONSUMPTION', 'CALCULATED PRICE']
table.align["MEASUREMENT"] = 'r'
table.align["CONSUMPTION"] = 'r'
table.align["CALCULATED PRICE"] = 'r'

# Reads file and prints a PrettyTable to the terminal.
def readFile():
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

readFile()