# Write a program to find the remainder when an integer A is divided by an integer B.
#

n = int(input())
for i in range(0, n):
    a, b = map(int, input().split())
    print(a%b)