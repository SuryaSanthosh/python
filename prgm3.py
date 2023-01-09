import csv

#open the csv file
with open('data.csv','r')as file:
   # create a CSV reader
   reader=csv.reader(file)

   #Iterate over the rows of the CSV file
   for row in reader:
       # print the row as a list of strings
       print(row)
