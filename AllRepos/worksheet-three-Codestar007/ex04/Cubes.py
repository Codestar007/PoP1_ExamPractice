n, m = [int(x) for x in input().split(' ')]
N = {int(input()) for i in range(n)}
M = {int(input()) for x in range(m)}
NuM = N.intersection(M)

C = []
C.append(NuM)
C.append(N.difference(M))
C.append(M.difference(N))

for i in range(len(C)):
    print(len(C[i]))
    C1 = list(C[i])
    C1.sort()
    for elem in C1:
        print(elem)
