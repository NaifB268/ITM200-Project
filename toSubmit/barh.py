import csv
import calendar
import matplotlib.pyplot as plt
a = 0
b = 0
saleslast2021 = []
saleslast2022 = []
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
saleslast2022 = [val+(val*growth) for val in saleslast2021]


fig, ax = plt.subplots()
ax.barh(monthslast, saleslast2022)
plt.subplots_adjust(left=0.2, right=0.9, top=0.9, bottom=0.1)

plt.title("Estimated sales for year 2022 from month of July to December") # Writing plot title
plt.xlabel("Estimated Sale")      # Writing x-axis label
plt.ylabel("Months")  # Writing y-axis label

plt.show()
fig.savefig('barploth.png')