# Write a Python program that checks if a number is prime or not.
#
# If the number is prime, it should print "Prime".
#
# If the number is not prime, it should print "Not prime".

n = 12
flag = 1
for i in range(2, n):
    if n % i == 0:
        flag = 0
        break
if flag:
    print("Prime")
else:
    print("Not Prime")