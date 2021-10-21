# A 5 match test series between India and England has just concluded.
#
# Every match could have ended either as a win for India, a win for England, or a draw. You know the result of all the matches. Determine who won the series or if it ended in a draw.
#
# A team is said to have won the series if it wins strictly more test matches than the other team.
#
# Input Format
# First-line will contain T, the number of test cases. Then the test cases follow.
# Each test case contains a single line of input, five space-separated integers R1,R2,R3,R4,R5 denoting the results of all the five matches. Ri=0 denotes that the test match ends in a draw. Ri=1 denotes that the test match is won by India. Ri=2 denotes that the test match is won by England.
# Output Format
# For each test output "DRAW" if the series ends in a draw, "INDIA" if the series is won by India, and "ENGLAND" if the series is won by England.
#
# You may print each character of the string in uppercase or lowercase (for example, the strings "dRaw", "draw", "Draw" and "DRAW" will all be treated as identical).
#
# Constraints
# 1≤T≤1000
# 0≤Ri≤2
# Sample Input 1
# 3
# 0 1 2 1 0
# 0 1 2 1 2
# 2 2 2 2 1
# Sample Output 1
# INDIA
# DRAW
# ENGLAND

n = int(input())
r = []
for i in range(0, n):
    a = input()
    list = a.split()
    r.append(list)

for k in r:
    # print(k)
    # print(type(k))
    x = k.count('0')
    y = k.count('1')
    z = k.count('2')
    if y == z :
        print("DRAW")
    elif y > z:
        print("INDIA")
    else:
        print("ENGLAND")