import csv
#specify the column indices that you want to read
# e.g.column 0 is the first column ,column is the second column ,etc
columns_to_read=[0,2]

#open the csv file and read the contents
with open('dataa.csv','r') as f:
    clmn_reader=csv.reader(f)

        #iterate over the rows of the csv
        for row in clmn_reader:
            #print the conents of the specified columns
            print([row[i]for i in columns_to_read])
