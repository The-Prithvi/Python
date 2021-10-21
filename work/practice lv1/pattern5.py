'''
    *
  * * *
* * * * *
'''
def odd(n):
    if n % 2 == 0:
        return True
    else:
        return False


n = 7
for i in range(n-1 , -1, -1):
    for j in range(i, 0, -1):
        print(" ", end=" ")
    if odd(i):
        print(("*" + "   ")*(n-i), end=" ")
        continue
    # else:

    print()

