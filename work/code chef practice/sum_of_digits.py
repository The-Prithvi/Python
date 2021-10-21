# # You're given an integer N. Write a program to calculate the sum of all the digits of N.
#
n = int(input())
for i in range(0, n):
    a = int(input())
    ans = 0
    while(a > 0):
        ans = ans + (a%10)
        a = a//10
    print(ans)


