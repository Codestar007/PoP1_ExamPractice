m, n = [int(i) for i in input().split()]
a = [[int(i) for i in input().split()] for x in range(m)]
c = int(input())
for row in a:
    for elements in row:
            print(elements*c, end=' ')
    print()
