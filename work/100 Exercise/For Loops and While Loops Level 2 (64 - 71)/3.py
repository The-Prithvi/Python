# Write a Python program that prints the digits of a number in reverse order on the same line.
#
# If the number only has one digit, print this digit.

n = 5061
# n = 111
while(n > 0):
    print(n%10, end="")
    n = n//10