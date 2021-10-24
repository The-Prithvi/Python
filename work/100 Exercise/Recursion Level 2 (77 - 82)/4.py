# Write a Python program that converts a decimal number to binary using recursion.
#
# The function must return the binary representation as a string.
#
# The program must print the value returned.
li = []
def bin(n):
    if n//2 == 0:
        li.append(n % 2)
    else:
        li.append(n % 2)
        bin(n//2)

bin(567)
print(li[::-1])