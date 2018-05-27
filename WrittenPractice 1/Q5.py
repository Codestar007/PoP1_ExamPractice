"""
Given an integer `n` as an argument, the points function creates a dictionary object and populates it with a name `n` number of
Keys in alphabetical order and randomly generated tuple values.

"""

import random
def points(n):
    directory = {}
    for i in range(0, n):
        pname = chr(ord("a") + i)
        x = 1000.0 * random.random()
        y = 1000.0 * random.random()
        directory[pname] = (x, y)
    return directory

print(points(5))