"""Generate the list of random numbers produced by a certain range of seeds"""
import random

for t in range(1, 11):
    random.seed(t)
    text1 = "Seed (" + str(t) + "): "
    for i in range(11):
        text1 = text1 + "," + str(random.randint(1, 6))
    print(text1)
