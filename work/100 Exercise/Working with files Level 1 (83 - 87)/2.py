# Write a Python program that reads a text file and prints the first n lines of the file.
#
# The value of n should be entered by the user.
#
# If the value of n is greater than the total number of lines in the file, print
#
# "Please enter a value for n. The file has <num_lines> lines".

n = 2
f = open("1.txt", "r")
# for i in range(0, n):
#     print(f.readline(), end="")

# ++++++++++++++++++++ OR ++++++++++++++++++++
c = f.readlines()
for i in range(n):
    print(c[i].strip('\n'))
f.close()