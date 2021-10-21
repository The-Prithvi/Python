# Write a Python program that check if a string only contains numbers.
#
# If it does, print True. Else, print False.

# s = input("string: ")
# s = "prithvi20"
# s = ""
# s = "prithvi"
s = "123"

for i in s:
    if i.isdigit() == True:
        print("True")
        break
else:
    print("False")