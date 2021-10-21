# Write a Python program that prints the number of days in a given month.
#
# The value of the variable month is the name of the month with the first letter capitalized.
#
# Do not consider leap years for the number of days in February.
#
# You can add a customized message. For example: "<month> has: <num_days> days."
# month = "jan"
month = "feb"
# month = "nov"
monthfeb = ["feb"]
month31 = ["jan", "mar", "may", "jul", "aug","oct", "dec"]
month30 = ["apr", "june", "sept", "nov"]

if month in monthfeb:
    print("28 Days")
elif month in month30:
    print("30 Days")
elif month in month31:
    print("31 Days")

