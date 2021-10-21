# Write a Python program that reverses the individual words in the string s and changes their capitalization. Uppercase letters should be printed in lowercase and vice versa.
#
# Assume that the string only contains letters and spaces are used to separate words.

s = "Hello World"
sli = s.split(" ") #-->Making List of s
ans = ""
print(s)
for i in sli:
    reverse = i[::-1]  #-->Reversing the word
    swap = reverse.swapcase()  #-->Swapping upper and lower
    ans += swap + " "

print(ans)


