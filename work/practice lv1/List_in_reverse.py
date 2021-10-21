li = [10, 20, 30, 40, 50]
for i in range(len(li)-1, -1, -1):
    print(li[i], end=" ")
print()

    # Method2
li1 = [10, 20, 30, 40, 50]
new_list = reversed(li1)
for item in new_list:
    print(item, end=" ")