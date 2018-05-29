n = int(input())
r = [['.'] * n for i in range(n)]

for i in range(n):
    r[i][n//2] = '*'
    r[i][i] = '*'
    r[i][n-i-1] = '*'
    r[(n//2)][i] = '*'
for row in r:
    print(' '.join([str(elem) for elem in row]))
