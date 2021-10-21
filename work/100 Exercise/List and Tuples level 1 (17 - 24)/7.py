# Write a Python program that removes duplicate elements from a list, only keeping one occurrence of each element in the list.
#
# The original list should be mutated (modified).
#
# The program must print the final version of the list.

li = [1,1,2,3,4,4]
li2 = []
for i in li:
    if li.count(i)>1:
        li.remove(i)
print(li)