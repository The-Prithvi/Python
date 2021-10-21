# -> Write a Python program that prints the character at index i in the string s.
#
# -> If the index is out of range, the program should print "i is out of range"
#
# -> If the string is empty, the program should print "Empty String"

s1 = "Prithvi is a good boy"
i = int(input("enter index: "))
if i <= len(s1):
    print(s1[i])
elif len(s1) == 0:
    print("Empty string")
else:
    print("Index is out of range")
