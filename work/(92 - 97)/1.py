# Write a Python program that displays the current date and time.
#
# The program should print Current Date and Time: on the previous line.
#
# The date should be formatted as YYYY-MM-DD
#
# The time should be formatted as HH:MM:SS
#
# 🔹 Expected Output:
# This will depends on the date and time when the program is executed, but this is an example of the expected output:
#
# Current Date and Time:
# 2021-02-26 13:31:08
import datetime

import datetime
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))