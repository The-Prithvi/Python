# Write a Python program that checks if a file exists in the specified path or not.
#
# If it exists, print "The file <file_name> exists"
#
# If it doesn't, print "The file <file_name> doesn't exist"
#
# The file name could also be an absolute path to the file.

import os

a = "3.txt"
b = os.path.isfile(a)
if b:
    print( "{} File Exists".format(a))
else:
    print("{} File Doesn't Exists".format(a) )
