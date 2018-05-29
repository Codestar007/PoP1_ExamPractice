a = [int(i) for i in input().split(' ')]
m = a[0]
n = a[1]

max_elem = 0
max_index = 0, 0
for i in range(m):
    a = [int(x) for x in input().split(' ')]
    if i == 0:
            max_elem = a[i]
    for j in range(n):
        if a[j] > max_elem:
            max_elem = a[j]
            max_index = i, j
print(' '.join([str(elem) for elem in max_index]))
