# Write a Python program that checks if a string is a palindrome or not (if it's read the same backwards and forwards).
#
# The program should be case-insensitive. Therefore, "A" should be considered equivalent to "a".
#
# Print True if the string is a palindrome. Else, print False.
#
# If the string is empty, print True.

def pal(s):
	s = s.lower()
	if len(s) <= 1:
		return True
	elif s[0] != s[-1]:
		return False
	else:
		return pal(s[1:-1])   #Reducing String

print(pal("hello"))
print(pal("Anna"))


#illustration ->

# first call:
# 1st condition fail
# 2nd condition fail
# now at 3rd call 'anna' is reduced to 'nn'
# now again same process
