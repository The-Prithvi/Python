# The first line contains an integer T, the total number of test cases. Then follow T lines, each line contains an integer N.

n = int(input())
for i in range(0, n):
    a = input()
    a1 = int(a[len(a)-1])
    a2 = int(a[0])
    print(a1+a2)
