# Write a Python program that prints a list with the elements that listA and listB have in common.
#
# If they don't have any elements in common, print an empty list.
#
# The program should not assume that the lists have the same length.
#
# You may assume that each element will only appear once in each list.

a = [1,2,3,4]
b = [8,4,10,1]
seta = set(a)
setb = set(b)
final = seta.intersection(setb)
print(final)