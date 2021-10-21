# Write a Python program that prints the maximum of three integers (a, b, c).

a = 5
b = 5
c = 5
max = a
if a>b and a>c:
    max = a
elif b>a and b>c:
    max = b
elif c>a and c>b:
    max = c
print(max)