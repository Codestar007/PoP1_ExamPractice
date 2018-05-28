# x = [1,2,3,4,5]
# print(x[::-1]) ##Reverse
# print(x[-1:-3:-1])
# print(x[-2:-3:-1])
#
# print(lambda x:(x*2 for x in range(3)))
#
#
# s = set([1,2,3])
# t = set([3,4,5])
#
# print(s.union(t))
# print(s.difference(t))
# print(s.intersection(t))
# print(s.isdisjoint(t))
# print(s.issubset(t))
# print(s.issuperset(t))
#
# ##Lambdas
# # The general syntax of a lambda function is quite simple:
# # lambda argument_list: expression
# a = [1,2,3,4]
# b = [17,12,11,10]
# c = [-1,-4,5,9]
# print(list(map(lambda x,y:x+y, a,b))) #[18, 14, 14, 14]
# print(list(map(lambda x,y,z:x+y+z, a,b,c))) #[17, 10, 19, 23]
# print(list(map(lambda x,y,z:x+y-z, a,b,c))) # [19, 18, 9, 5]
#
# isEven = lambda n: n % 2 == 0
# print(isEven(224))


columns, rows =  10, 10
#ten_by_tenList = [][]
result = [["None" for r in range(rows)] for c in range(columns)]
a = [[[None] * 10] * 10]


words = "How are you doing today sir"
for word in words.split(" "):
    print(word)

word = "Howdoyoudosir"
for ch in word:
    print(ch)


n, nums = 3, range(1, 6)
print(n, nums)

import copy
def duplicate(lst):
    return copy.copy(lst)


def test_duplicate():
    lst = [1,2,3,4,5]
    lstchanged = duplicate(lst).pop(1)
    assert lstchanged != lst

test_duplicate()

# Iteration VS Recursion
#
# ITERATION
def factorialIteration(num):
    answer = 1; #needs initialization
    for t in range(1, num + 1): #iteration
        answer *= t
    return answer

# RECURSION
def factorialRecursion(num):
    if num ==  1:#Base case
        return 1
    else:
        answer = factorialRecursion(num - 1) * num; # recursive calling
    return answer

num = 5
print("factorialIteration", factorialIteration(num))
print("factorialRecursion", factorialRecursion(num))


a = input("Type something: ")
print(str(a))