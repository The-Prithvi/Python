# Write a Python program that sorts (in ascending order) the lists contained as values in a dictionary.
#
# The dictionary contains key-value pairs that match strings to lists. You need to sort these lists.
#
# The lists have to be mutated (changed).
#
# 🔹 Expected Output:
# If this is the dictionary:
#
# my_dict = {"a": [4, 3, 2],"b": [5, 3, 7],"c": [1, 9, 10],"d": [3, 4, 1]}
# The final output should be:
#
# my_dict = {
# 	"a": [2, 3, 4],
# 	"b": [3, 5, 7],
# 	"c": [1, 9, 10],
# 	"d": [1, 3, 4]
# }
# Notice how all the lists are now sorted in ascending order.
#
# 🔸 Hints:
# The .sort() method sorts a list (the list is mutated/changed).
#
# Be careful with using sorted() because it only returns a sorted copy of the list.

a = {"a": [4, 3, 2],"b": [5, 3, 7],"c": [1, 9, 10],"d": [3, 4, 1]}
# a = {"a":1, "b":2, "c":3}
b = []
bkeys = []
c = {}
cnt = 0
for i in a.values():
    i.sort()
print(a)


