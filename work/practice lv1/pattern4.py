'''
    *
   * *
  * * *
 * * * *
* * * * *
'''
n = 5
for i in range(n , -1, -1):
    for j in range(i, 0, -1):
        print(" ", end=" ")
    print(("*" + "   ")* (n-i), end=" ")
    print()

