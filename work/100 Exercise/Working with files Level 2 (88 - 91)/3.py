# Write a Python program that copies the content of a file to another file.
#
# If the new file doesn't exist, the program should create it.

f = open("2.txt", "r")
f2 = open("3.txt", "w")

for i in f:
    f2.write(i)
