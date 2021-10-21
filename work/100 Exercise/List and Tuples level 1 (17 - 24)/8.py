# Write a Python program that counts the number of elements in a list with value greater than 3.
#
# You may assume that the list only contains numbers.
#
# Print the final count.

li = [4,8,1,3,2]
li2 = []
count = 0
for i in li:
    if i > 3:
        count += 1
        li2.append(i)
print(count)
print(li2)