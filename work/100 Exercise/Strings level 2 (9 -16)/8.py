# Write a Python program to convert a string s to lowercase, sort the characters of each word in alphabetical order, and print the resulting string.
#
# You may assume that the string only contains letters and spaces to separate the words.
#
# Spaces should be preserved in the final string.

s = "hello world"
sli = s.split(" ")
print(sli)
ans = ""
for i in sli:
    a = "".join(sorted(i))
    print(a)
    ans += a + " "
print(ans)