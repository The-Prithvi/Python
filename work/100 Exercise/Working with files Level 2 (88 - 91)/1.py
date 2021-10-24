# Write a Python program that writes the elements of a list to the file denoted by the variable file.
#
# Each element should be written on a separate line.
#
# The file should be new or its existing content must be replaced by this new content.
import os

a = [5,8,9,4,1,2,3]
f = open("li.txt", "w")
for i in a:
    f.write(str(i))



