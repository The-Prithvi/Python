# n = 7:

# ---*
# --***
# -*****
# *******
# -*****
# --***
# ---*

n = 15
for i in range((n//2), -1, -1):
    for j in range(i, 0, -1):
        print("  ", end="")
    print("* " * (n - i*2))

for i in range(1, (n//2)+1):
    for j in range(0, i):
        print("  ", end="")
    print("* " * (n - i*2))



