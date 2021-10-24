# Write a Python program that prints the last n lines of a text file in order.
#
# The value of n should be provided by the user.
#
# You may assume that n is a valid positive integer.

n = 2
f = open("1.txt", "r")
c = f.readlines()
for i in range(n, len(c)):
    print(c[i].strip('\n'))
f.close()