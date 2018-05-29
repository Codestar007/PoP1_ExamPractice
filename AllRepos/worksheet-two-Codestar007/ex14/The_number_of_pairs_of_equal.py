total = 0
a = [int(s) for s in input().split()]
for i in range(len(a)):
    t = a[i:len(a)]
    total += t.count(t[0])-1
print(total)
