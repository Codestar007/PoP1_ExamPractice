a = [int(s) for s in input().split()]
n, k = a[0], a[1]
start_pins = ["I"] * n

for i in range(0, k):
    knock_rng = [int(s) for s in input().split()]
    rng_lth = len(start_pins[knock_rng[0]-1:knock_rng[1]])
    start_pins[knock_rng[0]-1:knock_rng[1]] = rng_lth * "."
print(''.join([str(i) for i in start_pins]))
