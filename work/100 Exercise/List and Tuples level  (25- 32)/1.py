# Write a Python program that prints (as a list) the elements of listA that are not in listB as a list.
#
# If the lists have the same elements, print an empty list.
#
# If listA is an empty list, print an empty list.

li = [1,2,3,4]
li2 = [2,4,5,7]
# li2 = [1,2,3,4]
# li2 = []
set1 = set(li)
set2 = set(li2)
if set1 == set2:
    print("No Element found")
elif len(set1) == 0 or len(set2) == 0:
    print("No Elemnet found")
else:
    print(set1-set2)