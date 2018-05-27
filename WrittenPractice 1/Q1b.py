def get_perfect_numbers(n):
    result = []
    for i in range(1,n +1):
        total = 0
        for j in range(1, i):
            if i%j == 0:
                total += j
        if total == i:
            result.append(i)
    return result

n = 500
print(*get_perfect_numbers(n), sep = ", ")


#### OR
for i in range(1,501):
    total = 0
    for j in range(1, i):
        if i%j == 0:
            total += j
    if total == i:
print(i)