import re
txt = "Prithvi is a good boy"
# x = re.findall("^P", txt)
x = re.findall("boy$", txt)
if x:
    print("Yes")
else:
    print("No")