# Write a Python program that prints a version of the string s with all commas replaced by dots

# s = " Hello, Prithvi"
s = "12,123,4555"
for i in s:
    if i == ",":
        s1 = s.replace(i ,".")
        print(s1)
        break
else:
    print(s)