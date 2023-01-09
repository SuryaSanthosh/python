# specify the coloumn indicates that you want to read
# here column 0 is the first column,column 1 is the second column
columns_to_read=[0,2]

# open the csv file and read the contents
with open('data.csv','r') as f:
   clmn_reader = csv.reader(f)

   #Iterate over the rows of the csv
   for row in clmn_reader:
       # print the contents of the specified columns
       print([row[i] for i in columns_to_read])
