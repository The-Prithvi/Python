# Write a Python program that prints the first and last three characters of the string s as a single string.
#
# If the string has less than six characters, print an empty string (blank output).

# s = input("String: ")
s = "Wonderful"
s1 = ""
s2 = ""
if len(s) < 6:
    print("")
else:
    for i in range(len(s) - 3, len(s)):
        s2 = s2 +  s[i]
    for i in range(0, 3):
        s1 = s1 +  s[i]
print(s1 + s2)

