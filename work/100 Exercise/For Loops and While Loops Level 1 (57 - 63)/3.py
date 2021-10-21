# Write a Python program that calculates and prints the sum of the first 100 non-negative integers (from 1 to 100).
#
# Use a loop to find this sum.

sum = 0
for i in range(1, 101):
    sum = sum + i
print(sum)