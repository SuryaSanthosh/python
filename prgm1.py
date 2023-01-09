# program to read file content and store it into a list
# using readlines()
open_file = open("new.txt", "r")
File_lines = open_file.readlines() # stores all the lines in the file as list

# without using strip
print("\n File Content with new line character: ")
print(File_lines)

# By using Strip
print("\n File content after removing new line content: ")
File_lines = [X.strip() for X in File_lines]
print([X.strip() for X in File_lines])
open_file.close()
