m, n, r = [int(i) for i in input().split()]
A = [[int(i) for i in input().split()] for x in range(m)]
B = [[int(i) for i in input().split()] for x in range(n)]

for i in range(m):
    for t in range(r):
        total = 0
        for k in range(n):
            total +=  A[i][k] * B[k][t]
        print(total, end = ' ')
