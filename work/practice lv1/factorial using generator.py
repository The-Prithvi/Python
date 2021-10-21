def no(n):
    if n == 1 or n == 0:
        return 1
    return n * no(n-1)

def genno(n):
    for i in range(1, n + 1):
        yield no(i)

n = genno(6)
for i in n:
    print(i)