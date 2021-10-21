# Write a Python program that checks if a key exists in a dictionary or not.
#
# If the key exists in the dictionary, print True. Else, print False.
#
# The key should be stored in the variable key.

# Hints:
# The in operator can be very helpful to solve this challenge.

a = {"a":1, "b":2, "c":3}
# key = "a"
key = "d"
if key in a:
    print("True")
else:
    print("False")