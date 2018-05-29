N = int(input())
d_Files = {}
for i in range(N):
    A = input().split()
    d_Files[A[0]] = A[1:]

M = int(input())
for i in range(M):
    B = input().split()
    if B[0] == 'write':
        B[0] = 'W'
    elif B[0] == 'read':
        B[0] = 'R'
    elif B[0] == 'execute':
        B[0] = 'X'
    
    if B[0] in d_Files.get(B[1]):
        print("OK")
    else:
        print("Access denied")