# Write a Python program that prints the string s without the character at index n.
#
# If the index n is out of range, print the string s intact.
#
# If the string s is empty, print the string s intact.

# n = input("Index: ")
n = 1
s = "prithvi"
# s = ""
s1 = ""
s2 = ""
if n >= len(s) or len(s) == 0:
    print(s)
else:
    for i in range(0, n):
        s1 = s1 + s[i]
    for i in range(n+1 , len(s)):
        s2 = s2 + s[i]

print(s1 + s2)
