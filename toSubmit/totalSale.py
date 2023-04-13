import csv

years = []
totals = []
with open('Data.csv', mode='r') as fileCSV:  # Opening the sample.csv file
    fCSV = csv.reader(fileCSV)  # Reading the csv file
    next(fCSV) # skip header
    for line in fCSV:
        if 2012 <= int(line[0]) <= 2021:
            years.append(line[0])
            totals.append(str(sum(int(x) for x in line[1:])))


with open('stats.txt', 'w') as outfile:
    outfile.write("Total Sales from year 2012 to 2021\n")
    for i, year in enumerate(years):
        outfile.write(f'{year}: {totals[i]}\n')
