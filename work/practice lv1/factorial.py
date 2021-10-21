n = int(input())
res = 1
print(str(n) + "!", end="= ")
for i in range(n, 0, -1):
    res = i * res
    if(i!=1):
        print(str(i), end="x")
    else:
        print(str(i), end=" = ")
print(res)
