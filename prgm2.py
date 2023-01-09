# program to copy odd lines of one file to another
input_file = open("new.txt")
output_file = open("writedata.txt",'w')
# copying/reading contents from read_file to write_file
copy_data = input_file.readlines()
print("Actual file content is: ")
print(copy_data, "\n")
for i in range(0, len(copy_data)):
   if i % 2 == 0:
       output_file.write(copy_data[i])
   else:
       pass

# closing file after writing
output_file.close()

# opening write file in read mode and printing values
output_file = open("writedata.txt", 'r')
print("odd lines are: ")
print(output_file.read())

# closing files
input_file.close()
output_file.close()
