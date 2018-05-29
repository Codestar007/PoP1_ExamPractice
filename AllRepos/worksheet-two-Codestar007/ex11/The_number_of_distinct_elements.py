a = input().split()
uniq_lst = []

for i in range(len(a)):
    if int(a[i]) not in uniq_lst:
        uniq_lst.append(int(a[i]))
print(len(uniq_lst))
