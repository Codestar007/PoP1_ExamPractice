########################################################
###MAP
# Python program to demonstrate working of map.
########################################################
# Return double of n
def addition(n):
    return n + n

# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

# Double all numbers using map and lambda

numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))

a = [1,2,3,4,5]
# print(map(list, a))
def doubleNum(n):
    return n*2

# result = list(map(lambda x: x + x, a))
result = list(map(doubleNum, a))
result2 = list(filter(lambda x: (x % 2 == 0), a)) # filter out Odd numbers
print(*result, sep=" - ")
print(list(reversed(a)))
print(result2)
# result = map(doubleNum, a)
# print(*tuple(result), sep="\n")
#print(tuple(i*2 for i in a))

########################################################
#FILTER
########################################################
# Python Program to find palindromes in
# a list of strings.

my_list = ["geeks", "geeg", "keek", "practice", "aa"]

# use anonymous function to filter palindromes.
# Please refer below article for details of reversed
result = list(filter(lambda x: (x == "".join(reversed(x))), my_list))

# printing the result
print(result)

########################################################
#ZIP
########################################################
# Python code to demonstrate the application of
# zip()

# initializing list of players.
players = ["Sachin", "Sehwag", "Gambhir", "Dravid", "Raina"]

# initializing their scores
scores = [100, 15, 17, 28, 43]

# printing players and scores.
for pl, sc in zip(players, scores):
    print("Player :  %s     Score : %d" % (pl, sc))

    # Output:
    #
    # Player: Sachin
    # Score: 100
    # Player: Sehwag
    # Score: 15
    # Player: Gambhir
    # Score: 17
    # Player: Dravid
    # Score: 28
    # Player: Raina
    # Score: 43


########################################################
#Dictionary
########################################################
d = {} # empty

d = {"Myname":"kiz","House":34}
print("Name:", d.get("Myname"))

d2 = dict(zip(players,scores))
print("score:", d2.get("Sachin"))

for k, v in d2:
    print("player:",d2.k, "Score:",str(d2.v))

# Create a new dictionary
d = dict()  # or d = {}

# Add a key - value pairs to dictionary
d['xyz'] = 123
d['abc'] = 345

# print the whole dictionary
print(d)

# print only the keys
print(d.keys())

# print only values
print(d.values())

# iterate over dictionary
for i in d:
    print("%s  %d" % (i, d[i]))

# another method of iteration
for index, value in enumerate(d):
    print(index, value, d[value])

# check if key exist
print('xyz' in d)

# delete the key-value pair
del d['xyz']

# check again
print("xyz" in d)