# Write a Python program to count the number of repeated characters in the string s.
#
# The program must print the total number of repeated characters and a message on the next line displaying the repeated characters separated by a space and sorted alphabetically.
#
# If there are no repeated characters in the string, print 0 as the total count and None on the next line.

s = "corporation"
count = 0
repeated_chars = []

for i in s:
    if(s.count(i)>1) and (i not in repeated_chars):
        count += 1
        repeated_chars.append(i)
print("No.Of Charecters:" ,count)
print(repeated_chars)





