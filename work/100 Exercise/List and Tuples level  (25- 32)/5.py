# Write a Python program that prints the second smallest value in a list.
#
# If the list is empty or only has one element, print None.

a = [4,1,5,6,2]
# a = [5]
# a = []
if len(a)<=1:
    print("None")
else:
    sortedli = sorted(a)
    print(sortedli[1])