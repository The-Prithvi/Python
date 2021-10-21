# Q. Use a loop to display elements from a given list present at odd index positions
li = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in range(len(li)):
    if(i%2 != 0):
        print(li[i], end=" ")