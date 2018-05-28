mylist = [1,2,3,4,5]

#A
def printList(mylist):
    for elem in mylist:
        print(elem)
printList(mylist)

#B
mylist2 = [1,2,3,4,5]
i = 0
while (i < len(mylist2)):
    print(mylist2[i])
    i += 1

#C
mylist3 = [1,2,3,4,5]
for i in range(len(mylist3)):
    print(mylist3[len(mylist3)- (1+i)])

#D
x = -54
if x < 0:print("negative")
elif x == 0: print("Zero")
else: print("positive")

##value_true if <test> else value_false

#E
list = [1,2,3,4,5]
file = open("foo.txt", 'w')
for item in list:
    file.write(str(item) + '\n')
file.close()

#F
def isEven(x):
    return x%2 == 0
#G
def test_collatz():
    assert collatz(7) == 22
#H
def test_evenRand():
    assert evenRand() % 2 == 0

#I
def test_randBuzz():
    assert randBuzz() > 0 or randBuzz == "buzz"

#J
columns, rows =  10, 10
#ten_by_tenList = [][]
result = [["None" for r in range(rows)] for c in range(columns)]
print[result]

a = [[[None] * 10] * 10]

# OR

a = [ ]
    for i in range(0, 10):
    a.append(10 * [None])