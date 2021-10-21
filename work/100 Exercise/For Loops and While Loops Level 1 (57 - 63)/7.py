# Write a Python program that calculates the factorial of a given number n.
#
# The value of n should be entered by the user.
#
# The program must print the result and use a loop to calculate it.
#
# The factorial of a number n is denoted as n! and it is the result of multiplying all the positive integers that are less than or equal to n.
#
# For example, 3! = 3 * 2 * 1.
#
# 0! is equal to 1.

n = 5
fact = 1
for i in range(n, 1, -1):
    fact = fact*i
print(fact)