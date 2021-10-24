# 📌 Description:
# Write a Python program that prints the pattern of asterisks shown below for a given value of n.
#
# The program must include a recursive function.
#
# n represents the number of rows in the resulting pattern and the number of asterisks printed on the first row.
#
# 🔹 Expected Output:
# For n = 6:
#
# ******
# *****
# ****
# ***
# **
# *
# For n = 3:
#
# ***
# **
# *
# For n = 1:

def pat(n):
    if n == 1:
        print('* ')
    else:
        print('* ' * n)
        pat(n-1)
pat(5)