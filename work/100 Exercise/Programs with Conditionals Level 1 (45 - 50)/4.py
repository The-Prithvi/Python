# Write a Python program that prints the corresponding season based on the value of the variable season_num.
#
# The possible values of season_num are: 1 for Spring, 2 for Summer, 3 for Fall, 4 for Winter.
#
# If the value of season_num is neither one of these values, print "Please enter a valid number".

season_num = int(input())

if season_num == 1:
	print("Spring")
elif season_num == 2:
	print("Summer")
elif season_num == 3:
	print("Fall")
elif season_num == 4:
	print("Winter")
else:
	print("Please enter a valid number")