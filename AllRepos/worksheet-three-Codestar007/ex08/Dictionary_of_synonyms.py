a = int(input())
A = dict([input().split() for i in range(a)])
key = input()
syn = A.get(key, None)
if syn == None:
    for k, v in A.items():
        if v == key: print(k)
else:
    print(syn)