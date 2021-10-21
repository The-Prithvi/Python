# Write a Python program that prints the smallest value in a dictionary.
#
# If the dictionary is empty, print None.
#
# You may assume that the values are numeric.

a = {"a":1, "b":2, "c":3}
if a:
    print(min(a.values()))
else:
    print("Empty")