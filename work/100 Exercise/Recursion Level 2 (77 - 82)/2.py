# Write a Python program that counts the number of vowels in a string recursively.
#
# If the string is empty or only contains one consonant, print 0.
#
# The program should be case-insensitive. Therefore, vowels in uppercase should also be counted.

def count_vowels(string):
	string = string.lower()
	if not string:
		return 0
	elif string[0] in ("a", "e", "i", "o", "u"):
		return 1 + count_vowels(string[1:])
	else:
		return count_vowels(string[1:])