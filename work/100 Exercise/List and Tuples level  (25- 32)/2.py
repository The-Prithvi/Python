# Write a Python program that calculates the distance between two 3D points.
#
# The points are represented by two lists with three elements. The first element is the x-coordinate.
# The second element is the y-coordinate. The third element is the z-coordinate.
#
# Formula to find the Distance:
# AB = ((x2-x1)^2 + (y2-y1)^2 + (z2-z1)^2)^1/2
# Where: A(x1, y1, z1) and B(x2, y2, z2)

a = [3, 4, 5]
b = [1, 3, 5]
# a = [1,3,5]
ans = 0
for i in range(0, len(a)):
    ans += (b[i] - a[i])**2
print((ans)**(1/2))