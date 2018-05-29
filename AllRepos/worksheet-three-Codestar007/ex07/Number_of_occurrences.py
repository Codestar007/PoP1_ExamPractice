import copy
a = input().split(" ")
s = []

for i in range(len(a)):
    if a[i] in a[0:i]:
        t = copy.deepcopy(a[0:i])
        s.append(t.count(a[i]))
    else:
        s.append(0)
print(' '.join([str(e) for e in s]))