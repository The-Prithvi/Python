# Write a Python program that prints the positive and negative solutions (roots) for a quadratic equation.
#
# If the equation only has one solution, print the solution as the output.
#
# If it has two solutions, print the negative one first and the positive one second on the same line.
#
# If the equation has no real solutions, print "Complex Roots".
#
# You can determine the number of solutions with the discriminant (the result of b^2 - 4ac in the formula below).
#
# - If it's negative, the equation has no real solutions (only complex roots).
#
# - If it's 0, there is only one solution.
#
# - If it's positive, there are two real solutions.

a = 1
b = 2
c = 1
d = (((b)**2)-(4*(a)*(c)))**0.5
if d < 0:
    print("Complex Roots")
elif d == 0:
    print(((-b)+d)/(2*a))
else:
    print(((-b) - d) / (2 * a))
    print(((-b) + d) / (2 * a))
