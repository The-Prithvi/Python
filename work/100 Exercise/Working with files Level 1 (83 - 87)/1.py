# Write a Python program that reads a text file and saves its content line by line to a list called file_content.
#
# The list should contain strings that represent each line of the text file.
#
# The program should print the resulting list.

f = open("1.txt", "r")
c = f.readlines()
print(c)
f.close()