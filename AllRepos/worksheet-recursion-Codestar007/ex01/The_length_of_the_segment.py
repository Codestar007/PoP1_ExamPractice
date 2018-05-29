import math
x1, y1, x2, y2 = [float(input()) for i in range(4)]

def dist_calc(x1, y1, x2, y2):
    x, y = (x2 - x1)**2, (y2 - y1)**2
    d = math.sqrt(x + y)
    return d
print(dist_calc(x1, y1, x2, y2))