# Write a Python program that multiplies all the items in a list by the value of the variable factor.
#
# The program must print the list as the output.
#
# The program should also allow multiplying the variable factor by a string in case the list contains strings.
#
# You may assume that the value of factor will be a positive integer.

factor = 2
li = [3, 4 , 5, 6]
# li = ["a" , "b", "c"]
li2 = []
for i in li:
    li2.append(i*factor)

print(li)
print(li2)