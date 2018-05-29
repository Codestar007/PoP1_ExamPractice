a = [int(s) for s in input().split()]
for i in range(len(a)):
    if i > 0 and a[i] > a[i-1]:
        print(a[i], end = ' ')
