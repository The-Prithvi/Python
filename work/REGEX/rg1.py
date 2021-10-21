import re
txt = "Prithvi is a good boy and he 19 yrs old"
# x = re.findall("g..d", txt)
# x = re.findall("\d", txt)
# x = re.findall("od*", txt)
# x = re.findall("od+", txt)
x = re.findall("o{2}", txt)
print(x)
