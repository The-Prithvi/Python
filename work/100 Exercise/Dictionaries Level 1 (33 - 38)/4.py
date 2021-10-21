# Write a Python program that adds a new key-value pair to a dictionary only if the key doesn't exist already.
#
# If the key-value pair exists in the dictionary, do not update the existing value. The dictionary should not be modified in this case.
#
# Store the new key in the new_key variable and the new value in the new_value variable.
#
# Print the final value of the dictionary.
#
# Hints:-
# You can use the not in operator to check if a key is not in a dictionary.

a = {"a":1, "b":2, "c":3}
new_key = "d"
new_value = 4
if new_key not in a:
    a[new_key] = new_value
print(a)
