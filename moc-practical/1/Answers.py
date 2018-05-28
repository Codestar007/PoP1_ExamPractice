########################################
# Question 1
########################################

def fibonacci(num):
    if num == 0:
        return 0
    elif num <= 2:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

#print(*list(map(fibonacci, range(20))), sep=" ")


# OR

# prev = 0
# curr = 1
# print(prev, curr, end=" ")
# for x in range(3, 20 + 1):
#     next = prev + curr
#     print(next, end=" ")
#     prev = curr
#     curr = next

########################################
# Question 2
########################################

# myList = list(filter(lambda x: x < 2000, list(map(fibonacci, range(20)))))
# print()
# print(*myList, sep=" ")
# print("Length of list: ", len(myList))

# OR

prev = 0
curr = 1
counter = 2
print(prev, curr, end=" ")

# two terms printed so far
next = prev + curr
while next <= 2000:
    print(next, end=" ")
    counter += 1
    # shift the terms
    prev = curr
    curr = next
    next = prev + curr
print("\n", counter)