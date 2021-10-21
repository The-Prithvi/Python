def power(n1, n2):
    if (n1 == 0 or n1 == 1 or n2 == 1):
        return n1
    if (n2 == 0):
        return 1
    return n1 * power(n1, n2-1)
print(power(25,2))