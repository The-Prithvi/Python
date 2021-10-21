# # Write a Python program that prints a triangular pattern made with letters
#
# If the value of n is 3, this is the expected output:
#
# A
# B B
# C C C
# If the value of n is 5, this is the expected output:
#
# A
# B B
# C C C
# D D D D
# E E E E E
#
#
# 🔸 Hints:
# The chr() function converts a number to its corresponding character.
#
# The ASCII code points for uppercase letters start at 65 for "A".

n = 5
a = 65
for i in range(n+1):
    for j in range(i):
        print(chr(a-1), end=" ")
    a+=1
    print("")
