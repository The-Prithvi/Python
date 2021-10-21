a = [1,2,3,4,5,6,7,8,9,10]
b = [2,2,2,2,2,2,3]
print(any(x == 3 for x in a))
print(all(x == 3 for x in a))
print(any(x == 3 for x in b))
print(all(x == 2 for x in b))