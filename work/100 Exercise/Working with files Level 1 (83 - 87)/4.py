# Write a Python program that finds and prints the longest word in a text file.
#
# For this challenge, you may assume that the file only contains one word per line.
#

f = open("2.txt", "r")
c = f.readlines()
# print(c)
maxi = []
for i in c:
    maxi.append(len(i)-1)
# print(maxi)
m = max(maxi)
mpos = maxi.index(m)
print(c[mpos].strip("\n"))