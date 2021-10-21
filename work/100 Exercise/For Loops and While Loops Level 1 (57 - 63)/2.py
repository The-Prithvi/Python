# Write a Python program that prints the integers between a given number n and 1 (in descending order, both inclusive).
#
# The value of n should be entered by the user and you may assume that it is an integer greater than or equal to 1.
#
# Use a loop to print each number on a separate line.

n = 9
for i in range(n-1, 0, -1):
    print(i)