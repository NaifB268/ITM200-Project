import csv             
with open('Data.csv', mode = 'r') as fileCSV: # Opening the sample.csv file
    fCSV = csv.reader(fileCSV)                  # Reading the csv file
    for line in fCSV:
        print(line)                     # Printing file content line by line
  
