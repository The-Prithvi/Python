# Write a Python program that prints the largest of the values in a dictionary.
# You may assume that all the values in the dictionary are either lists or tuples.
#
# 🔹 Expected Output:
# If this is the dictionary:
#
# my_dict = {"a": [1, 2, 3],"b": [4, 0, -4],"c": [3, 5, 9],"d": [45, 12, 100]}
# This should be the output: 157

a = {"a": [1, 2, 3],"b": [4, 0, -4],"c": [3, 5, 9],"d": [45, 12, 100]}
b = []
for i in a.values():
    b.append(sum(i))
print(max(b))
