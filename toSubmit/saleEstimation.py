import csv
import calendar
a = 0
b = 0
saleslast2021 = []
with open('Data.csv', mode='r') as fileCSV:  # Opening the sample.csv file
    fCSV = csv.reader(fileCSV)  # Reading the csv file
    next(fCSV) # skip header
    for line in fCSV:
        if int(line[0]) == 2021:
            b = sum(int(x) for x in line[1:7])
            saleslast2021 = [int(x) for x in line[7:]]
        if int(line[0]) == 2022:
            a = sum(int(x) for x in line[1:7])

# Get the names of all months
months = list(calendar.month_name)

monthslast = months[-6:]
growth = (a - b)/a
# open the file in append mode
with open('stats.txt', 'a') as file:
    file.write(f"\nSales growth rate for the first 6 months of 2022: {growth}\n")
    file.write("\nEstimated sales for year 2022 from month of July to December\n")
    for i in range(len(saleslast2021)):
        file.write(f"{monthslast[i]} 2022: {int(saleslast2021[i] + (saleslast2021[i]*growth))}\n")