n = int(input())
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            a[i][j] = 0
        elif i < j:  # above main diagonal
            a[i][j] = j - i
        elif i > j:  # below main diagonal
            a[i][j] = i - j
for row in a:
    print(' '.join([str(elem) for elem in row]))

