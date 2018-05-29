A = {int(i) for i in input().split()}
B = {int(i) for i in input().split()}

D = list(A.intersection(B))
D.sort()
print(' '.join(str(i) for i in D))
