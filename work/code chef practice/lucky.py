# Output T lines. Each of these lines should contain the number of occurences of the digit 4 in the respective integer from Kostya's list.

n = int(input())
for i in range(n):
    a = input()
    b = a.count('4')
    print(b)