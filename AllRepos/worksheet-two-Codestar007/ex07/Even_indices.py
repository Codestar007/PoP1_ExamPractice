a = input()
s = a.split()
for elem in s[::2]:
    print(elem, end=' ')
