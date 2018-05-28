def calculatePower(a, n):
    result = 1
    if n == 0:
        result = 1
    elif n == 1:
        result = a
    else:
        result = result * a * calculatePower(a, n -1)
    return result

#print(calculatePower(2, 3))
assert calculatePower(2, 0) == 1
assert calculatePower(2, 1) == 2
assert calculatePower(2, 2) == 4
assert calculatePower(2, 3) == 8
assert calculatePower(2, 4) == 16
assert calculatePower(2, 5) == 32
assert calculatePower(2, 6) == 64
assert calculatePower(3, 3) == 27
