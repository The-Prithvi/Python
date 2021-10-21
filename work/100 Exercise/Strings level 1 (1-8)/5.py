# Write a Python program that prints the string s without the characters located at even indices.
#
# If the string is empty or only has one character, print it intact.

# s = input("String: ")
# s = "a"
# s= "coding"
# s = "Python"
s = ""
s1 = ""
for i in range(0, len(s)):
    if i % 2 != 0:
        s1  = s1 + s[i]
print(s1)
