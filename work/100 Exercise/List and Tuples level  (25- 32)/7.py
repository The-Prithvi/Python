# Write a Python program that prints a "flattened" version of a list that contains nested lists.
#
# "Flattened" means that all the elements in the nested lists should be added to a main list such that it doesn't contain any nested lists, just the individual.
#
# The list could contain other elements that are not lists or other sequences, so you must check the type of each element and act appropriately.
#
# If the list is empty, print an empty list.

a = [4, [1,2],[3,4],[5,6]]
b = []
for i in a:
    if isinstance(i, list):   # -> Checking if i is list or not
        for j in i:
            b.append(j)
    else:
        b.append(i)
print(b)
