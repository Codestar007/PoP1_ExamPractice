res = "NO"

curr_Q = [input().split() for s in range(8)]

for i in range(len(curr_Q)):
    next_Q = curr_Q[i+1:]
    for t in range(len(next_Q)):
        m, n = curr_Q[i], next_Q[t]
        x1, y1, x2, y2 = int(m[0]), int(m[1]), int(n[0]), int(n[1])
        if (x1 == x2) or (y1 == y2):
            res = "YES"
        elif abs(x1 - x2) == abs(y1 - y2):
            res = "YES"
print(res)
