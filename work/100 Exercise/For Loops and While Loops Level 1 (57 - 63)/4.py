# Write a Python program that prints the multiplication table for a positive integer n.
#
# The values displayed should go from n x 1 up to n x 10 with a descriptive format (as shown below).
#
# Use a loop to implement your solution.
#
# 🔹 Expected Output:
# If n is 3, this is the expected output:
#
# ==== Multiplication Table of 3 ====
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
# 3 x 4 = 12
# 3 x 5 = 15
# 3 x 6 = 18
# 3 x 7 = 21
# 3 x 8 = 24
# 3 x 9 = 27
# 3 x 10 = 30

n = 3
for i in range(1, 11):
    print(str(n) + " X " + str(i) + " = ", i*3)
