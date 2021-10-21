# Write a Python program that prints the second largest value in a list.
#
# If the list is empty or only has one element, print None.

a = [8,1,2,3,5]
# a = [1,2,3,4]
# a = [1,2]
# a = []

if len(a) <=1:
    print("None")
else:
    b = max(a)
    a.remove(b)
    print(max(a))

# +++++++++++++ OR +++++++++++++++
if len(a) <=1:
    print("None")
else:
    b = [8,1,3,5,4]
    sortedli = sorted(b)
    print(sortedli[-2])
