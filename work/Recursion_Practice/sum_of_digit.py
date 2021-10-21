def sum(n):
    if n == 0 or n == 1:
        return n
    return n%10 + sum(n//10)

print(sum(1041))