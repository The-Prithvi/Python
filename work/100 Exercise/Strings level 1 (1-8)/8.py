# Write a Python program that prints the string s with the character curr_char replaced by the character new_char.
#
# curr_char and new_char are variables that contain strings with a single character.
#
# You may assume that new_char will not be an empty string.
#
# The match must be case-sensitive (do not replace lowercase letters if curr_char is uppercase).
#
# If no match is found, print the initial string.

s = "hello"
c1 = "l"
c2 = "s"
s1 = s.replace(c1, c2)
print(s1)