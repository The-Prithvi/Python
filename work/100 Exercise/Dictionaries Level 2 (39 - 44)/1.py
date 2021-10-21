# Write a Python program that counts the frequency of each value in a dictionary.
#
# The program should create a new dictionary to map each value in the original dictionary to its frequency (how many times it occurs).
#
# If the dictionary is empty, print an empty dictionary.

a = {"a": 4,"b": 4,"c": 2,"d": 7,"e": 4,"f": 2,"g": 7,"h": 7}
b = []
e = {}
for i in a.values():
    b.append(i)
c = set(b)
d = list(c)
for j in d:
    e[j] = b.count(j)
print(e)

# ++++++++++++++ OR ++++++++++++++++++
other = {}

for i in a.values():
	if i in other:
		other[i] += 1
	else:
		other[i] = 1

print(other)
