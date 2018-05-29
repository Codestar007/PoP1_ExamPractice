N = int(input())
myD = {}
sortLst = []

for i in range(N):
    s = input()
    s = s.replace(' - ', ', ')
    s = s.split(', ')
    for d in range(1, len(s)):
        try:
            currval = myD[s[d]]
            myD[s[d]] = currval + ', ' + s[0]
        except KeyError:
                myD[s[d]] = s[0]

for key, val in myD.items():
    sortLst.append((key, val))
sortLst.sort(reverse=False)
print(len(myD))
for elm in sortLst:
    print(elm[0] + " - " + elm[1])

