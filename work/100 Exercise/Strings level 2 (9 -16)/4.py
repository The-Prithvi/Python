# Write a Python program that checks if the string s starts with the sequence of characters denoted by the variable prefix.
#
# If it does, print True. Else, print False.
#
# This test should be case sensitive. For example, "A" should not be equivalent to "a".
#
# If the length of the prefix is greater than the length of the string, print False.

s = "nora"
pre = "no"
ans = "False"
check = []
pre_len = len(pre)
if(len(pre)<= len(s)):
    for p in pre:
        check.append(p)
    for i in range(0, len(check)):
        if s[i] == check[i]:
            ans = "True"
        else:
            ans = "False"
    print(ans)
else:
    print("False")
