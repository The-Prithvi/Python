# Write a Python program that prints the largest value in a dictionary.
#
# If the dictionary is empty, print None.
#
# You may assume that the values are numeric.

a = {"a":1, "b":2, "c":3, "d":5}
if (len(a) == 0):
    print("Empty")
else:
    print(max(a.values()))