# Rock Paper Scissor

import random

print("Press '1' - stone")
print("Press '2' - paper")
print("Press '3' - scissor")
p = int(input("Enter 1 or 2 or 3: "))
stone = 1
paper = 2
scissor = 3
# b = random.randint(1,3)
b = 3
print("Bot = " +  str(b))
if p==b:
    print("Draw")
elif p==1 and b == 3:
    print("you won")
elif p == 2 and b == 1:
    print("you won")
elif p == 3 and b == 2:
    print("you won")
else:
    print("you lose")



