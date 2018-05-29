m, n = [int(x) for x in input().split(' ')]

A = []
for t in range(m):
    A.append(input().split())

i, j = [int(x) for x in input().split(' ')]

for y in range(m):
    A[y][i], A[y][j] = A[y][j], A[y][i]
    
for row in A:
    print(' '.join([str(elem) for elem in row]))