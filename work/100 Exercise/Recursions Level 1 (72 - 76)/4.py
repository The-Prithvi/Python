# Write a Python program that calculates and prints the sum of the digits of a positive integer num.
#
# The program must find the sum recursively.
#
# If the integer has only one digit, print the integer as the total sum.

def sumdig(n):
    if n == 0:
        return n
    return n%10 + sumdig(n//10)

print(sumdig(11))