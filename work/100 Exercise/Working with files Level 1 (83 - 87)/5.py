# Write a Python program that creates and prints a frequency dictionary of the words found in a text file.
#
# The keys of the dictionary should be the words in the file.
#
# The values should be their frequencies.
#
# You may assume that each line of the file only contains one word.

f = open('2.txt', "r")
final = {}
c = []
for i in f.readlines():
    c.append(i.strip('\n'))
for i in c:
    if i not in final:
        final[i] = 1
    else:
        final[i] += 1
print(final)