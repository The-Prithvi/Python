# This section tells us the format in which your program should give the output
# For each test case, add A and B and display the sum in a new line.

n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    print(a + b)
