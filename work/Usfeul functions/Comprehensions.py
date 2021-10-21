li = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
li2 = [i for i in li if i % 2 == 0]
print(li2)

di = {"Prithvi": 4, "Han": 7, "Dalmi": 21, "Piong": 41}
di2 = {j for j in di.values() if j > 10 }
print(di2)
