a = [int(s) for s in input().split()]
mini_idx, maxi_idx = a.index(min(a)), a.index(max(a))
a[maxi_idx], a[mini_idx] = min(a), max(a)
print(' '.join([str(i) for i in a]))
