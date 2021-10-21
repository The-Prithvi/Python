# occurance of  element in a list should be written in a dictionary where key is element and value is occurance

a = ["a", "a", "b", "c", "a", "b"]
b = {}
for i in a:
    b[i] = a.count(i)
print(b)