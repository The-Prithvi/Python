# If the value of n is 5:
#
# *
# * *
# * * *
# * * * *
# * * * * *
n = 5
for i in range(0, n):
    print("* "*i)

# ++++++++++++++++++++++++++ OR ++++++++++++++++++++++++

for i in range(0, n):
    for j in range(0, i):
        print("* ", end="")
    print("")