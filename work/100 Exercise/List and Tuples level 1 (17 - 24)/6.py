# Write a Python program that removes all occurrences of the element elem_to_remove from a list.
#
# The output of the program should be the new list with the element removed.
#
# If the element is not found in the list, print the message "Not Found".
#
# If the list is empty, print "Empty List".
n = 3
li = [3,3,2,1]
for i in range(0, li.count(n)):
        li.remove(n)
print(li)


