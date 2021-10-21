def sumli(list):
    if (len(list) == 1):
        return list[0]
    return (list[0] + sumli(list[1:]))

print(sumli([1, 2, 3, 4]))


