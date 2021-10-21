# Write a Python program that prints if a given year was (or will) be a leap year.
#
# Tip: A leap year is "a year, occurring once every four years, that has 366 days including February 29 as an intercalary day." (Definition by Oxford Languages).
#
# This is how you can determine if a year is a leap year or not:
#
# if (year is not divisible by 4) then (it is a common year).
#
# else if (year is not divisible by 100) then (it is a leap year)
#
# else if (year is not divisible by 400) then (it is a common year)
#
# else (it is a leap year)
#
# To learn more about leap years and how to determine if a year is a leap year or not, I recommend reading this resource.

year = 2017
if (year%4 !=00):
    print("it is a common year")
elif (year%100 != 0):
    print("it is a leap year")
elif (year%400 != 0):
    print("it is a common year")
else:
    print("it is a leap year")