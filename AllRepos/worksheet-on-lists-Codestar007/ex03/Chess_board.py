n, m = [int(i) for i in input().split(' ')]
a = []
for i in range(n):
    a.append(['.'] * m)

for i in range(n):  # iterate through rows 
    for j in range(m):  # iterate through columns
        if ((i + 1) % 2 > 0) and ((j + 1) % 2 > 0):
            a[i][j] = "."
        elif ((i + 1) % 2 == 0) and ((j + 1) % 2 > 0):
            a[i][j] = "*"
        elif ((i + 1) % 2 > 0) and ((j + 1) % 2 == 0):
            a[i][j] = "*"
for item in a:
    print(' '.join([str(s) for s in item]))
