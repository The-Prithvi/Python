# Write a Python program that prints a string reversed using a loop.
#
# All the characters must be on the same line in reverse order.

s = "Hello"
for i in range(len(s)-1, -1, -1):
    print(s[i], end="")