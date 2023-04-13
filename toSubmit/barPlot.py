
import matplotlib.pyplot as plt
import csv

years = []
totals = []
with open('Data.csv', mode='r') as fileCSV:  # Opening the sample.csv file
    fCSV = csv.reader(fileCSV)  # Reading the csv file
    next(fCSV) # skip header
    for line in fCSV:
        if 2012 <= int(line[0]) <= 2021:
            years.append(line[0])
            totals.append(sum(int(x) for x in line[1:]))

fig, ax = plt.subplots()
ax.bar(years, totals)


# Set the y-axis limit to start at zero
ax.set_ylim([0, max(totals) + 100000])
plt.title("Total Sales from year 2012 to 2021") # Writing plot title
plt.xlabel("Year")      # Writing x-axis label
plt.ylabel("Total Sales")  # Writing y-axis label

plt.show()
fig.savefig('barplot.png')



