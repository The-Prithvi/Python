# power

def expo(a, b):
    if b == 0:
        return 1
    return a * expo(a, b-1)
print(expo(2,3))