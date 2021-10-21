# Write a Python program that calculates and prints the nth Fibonacci number.
#
# The value of n represents the position of the element in the sequence.
#
# The initial value of n should be 0.
#
# You may assume that the value of n is a non-negative integer.

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89

def fibo(n):
    if n <= 1:
        return n
    else:
        return (fibo(n-1) + fibo(n-2))
a = 9
for i in range(a+1):
    print(fibo(i))