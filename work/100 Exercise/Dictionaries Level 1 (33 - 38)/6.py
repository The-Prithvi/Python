# Write a Python program that checks if all values in a dictionary are equal.
#
# If they are, print True. Else, print False.
#
# If the dictionary is empty, print "Empty".

a = {"a":1,"b":2, "c":3}
# a = {}
# a = {"a":2,"b":2, "c":2}
if a:
    b = list(a.values())
    if b.count(b[0]) == len(b):
        print("Equal")
    else:
        print("Not Equal")
else:
    print("Empty")

# ++++++++++++++++ OR ++++++++++++++++

c = set(a.values())
d = len(a)
if d == 0:
    print("empty")
elif d == 1:
    print("True")
else:
    print("False")