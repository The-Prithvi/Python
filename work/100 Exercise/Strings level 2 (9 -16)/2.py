# Write a Python program that checks if the string s contains all the letters in the alphabet (case-insensitive, so "A" should be equivalent to "a").
#
# If it does, print True. Else, print False.
#
# Before comparing the characters, you should convert the string to lowercase.
#
# If the string contains spaces, ignore them before finding the result.
#
# You may assume that the string doesn't contain any other symbols, only spaces (possibly).
#
# Consider these letters as part of the alphabet: 'abcdefghijklmnopqrstuvwxyz'

import string
s = "abcdefghijklmnopqrstuvwxyz"
# s = "DAX;MDCOJAS"
s1 = set(s.lower())
for i in s1:
    if i == " ":
        s1.remove(i)
print(s1 == set(string.ascii_lowercase))

 # +++++++++++++ OR +++++++++++++

import string

s2 = "The quick brown fox jumps over the lazy dog"
is_pangram = True

for i in string.ascii_lowercase:
    if i not in s2.lower():
        is_pangram = False
        break
print(is_pangram)