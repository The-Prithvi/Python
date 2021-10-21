# Write a Python program that prints the elements of a list followed their corresponding indices.
#
# Each element and its index must be on the same line separated by a space.
#
# If the list is empty, print "Empty List".

li = [5,4,2,63]
# li = []
for i in range(0, len(li)):
    print(str(i) + " " + str(li[i]) )