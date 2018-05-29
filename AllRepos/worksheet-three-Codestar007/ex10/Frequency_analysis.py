n = int(input())
myD = {}
sortLst = []
for i in range(n):
    RW = input().split(' ')
    for j in range(len(RW)):
        myD[RW[j]] = myD.get(RW[j], 0) + 1
for key, val in myD.items():
    sortLst.append((-val, key))
sortLst.sort()
for elm in sortLst:
    print(elm[1])
