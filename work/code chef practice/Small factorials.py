# For each integer n given at input, display a line with the value of n!

def fact(n):
    if n == 0 or n == 1:
        return n
    return n * fact(n-1)

n = int(input())
for i in range(n):
    a = int(input())
    print(fact(a))