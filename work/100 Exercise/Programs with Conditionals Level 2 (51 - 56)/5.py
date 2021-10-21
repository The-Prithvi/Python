# Write a Python program that simulates an interactive calculator with the basic arithmetic operations in Python (addition, subtraction, multiplication, division, integer division, and modulo).
#
# The program must interact with the user by asking for the values and the type of operation that will be performed.
#
# The output should include the values, the operation, and the result (as shown below).
#
# The type of operation will be denoted by an integer.
#
# - 1 for addition
#
# - 2 for subtraction
#
# - 3 for multiplication
#
# - 4 for division
#
# - 5 for integer division
#
# - 6 for modulo
#
# The program should present an initial message to the user describing the types of operations and the integer that has to be entered to select each one of them.
#
# If the values entered by the user are invalid for the operation selected, a descriptive message should be displayed. For example, for a division operation the denominator cannot be 0.
#
# If the user enters an invalid integer to select the operation, print
#
# "Please choose a valid operation"

ADDITION = 1
SUBTRACTION = 2
MULTIPLICATION = 3
DIVISION = 4
INTEGER_DIVISION = 5
MODULO = 6

print("=== Welcome to your Interactive Python Calculator ===")

a = int(input("Please enter the first value: "))
b = int(input("Please enter the second value: "))

print("Great! Now enter the operation.")
print("These are the available options:")
print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")
print("5 - Integer Division")
print("6 - Modulo")

operation = int(input("--> Enter the corresponding integer: "))

if operation == ADDITION:
	result = a + b
	print(f"The result of {a} + {b} is: {result}")
elif operation == SUBTRACTION:
	result = a - b
	print(f"The result of {a} - {b} is: {result}")
elif operation == MULTIPLICATION:
	result = a * b
	print(f"The result of {a} * {b} is: {result}")
elif operation == DIVISION:
	if b == 0:
		print("Division by Zero. Please enter another value for b.")
	else:
		result = a / b
		print(f"The result of {a} / {b} is: {result}")
elif operation == INTEGER_DIVISION:
	if b == 0:
		print("Division by Zero. Please enter another value for b.")
	else:
		result = a // b
		print(f"The result of {a} // {b} is: {result}")
elif operation == MODULO:
	result = a % b
	print(f"The result of {a} % {b} is: {result}")
else:
	print("Please choose a valid operation.")