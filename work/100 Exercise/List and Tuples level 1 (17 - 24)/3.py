# Write a Python program that prints the largest and smallest values in a list
#
# Print the two values on the same line, separated by a space.
#
# The largest value should appear first and the smallest value should appear second.
#
# You may assume that the list only contains numeric values.
#
# If the list is empty, print None.

# li = [-1, -2, -3 ,-4]
li = [0,0,0,0]
# li = []
if len(li) == 0:
    print("")
else:
    print(max(li), end=" ")
    print(min(li), end=" ")