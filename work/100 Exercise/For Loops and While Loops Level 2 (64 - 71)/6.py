# Floyd's Triangle:

# If n is equal to 3:
#
# 1
# 2 3
# 4 5 6
# If n is equal to 5:
#
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

n = 5
a = 1
for i in range(n+1):
    for j in range(i):
        print(a, end=" ")
        a+=1
    print("")