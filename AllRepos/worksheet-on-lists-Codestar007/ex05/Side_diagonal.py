n = int(input())
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            a[i][n-j-1] = 1
        if i > j:
            a[i][n-j-1] = 2
for row in a:
    print(' '.join([str(elem) for elem in row]))
