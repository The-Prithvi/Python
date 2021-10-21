# Write a Python program that prints a copy of the string s without any spaces.
#
# Words should be connected in the final string.
#
# If the string doesn't contain spaces, print it intact.a

# s = "hello, world"
# s = "python"
s = "Hello, World!"
s1 = ""

for i in s:
	if i != " ":
		s1 += i

print(s1)