# Pooja would like to withdraw X $US from an ATM. The cash machine will only accept the transaction
# if X is a multiple of 5, and Pooja's account balance has enough cash to perform the withdrawal ' \
#         'transaction (including bank charges). For each successful withdrawal the bank charges 0.50 $US.' \
#         ' Calculate Pooja's account balance after an attempted transaction

w, b = map(str,input().split())
w = int(w)
b = float(b)
if w % 5 == 0 and w <= b:
    print("{:.2f}".format(b - w - 0.50))
else:
    print("{:.2f}".format(b))