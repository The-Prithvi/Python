# Write a Python program that counts the number of characters in a file.
#
# Count all the characters in the file, including commas and quotes.
#
# Do not count spaces and remove \n (new line) characters.

a = ""
count = 0
f = open("2.txt", "r")
b = f.readlines()
for i in b:
    a = a + i.strip("\n")
for i in a:
    if i == " ":
        pass
    else:
        count += 1
print(count)