a = input().split()
res = ""
for i in a:
    if int(i)%2 == 0:
        res += str( " " + i)
print(res)
