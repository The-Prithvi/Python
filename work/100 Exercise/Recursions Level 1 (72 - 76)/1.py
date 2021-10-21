# Write a Python program that finds the sum of a list (or tuple) of numbers recursively.
#
# Print the total sum.
#
# If the list (or tuple) is empty, print 0.

def lisum(li):
    if len(li) == 0:
        return 0
    return li[0] + lisum(li[1:])   # li[:1] -> Means that removing element

a = [2, 8, 9, 1]
print(lisum(a))



