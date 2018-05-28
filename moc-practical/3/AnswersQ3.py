import math
import random

######################################
# Q1
######################################
# def checkListForNumber(orderedList, num):
#     return num in set(orderedList)
#
# ##Test
# orderedList = [1,2,3,4,5,6,7]
# assert checkListForNumber(orderedList, 7) == True
# assert checkListForNumber(orderedList, 9) == False

######################################
# Q2
######################################
# def checkForPrimeNumber():
#     #userInput = int(input("Please input a number: "))
#     for i in range(2,userInput):
#         if userInput % i == 0:
#             return False
#     return True
#print("Prime number?: ", checkForPrimeNumber())

# def is_prime(n):
#     if n == 2:
#         return True
#     if n % 2 == 0 or n <= 1:
#         return False
#
#     sqr = int(math.sqrt(n)) + 1
#
#     for divisor in range(3, sqr, 2):
#         if n % divisor == 0:
#             return False
#     return True

#userInput = int(input("Please input a number: "))
#print("Prime number?: ", is_prime(userInput))

######################################
# Q3
######################################

# userInput3 = input("Please input long string: ").split(" ")
# for i in range(len(userInput3)):
#     print(userInput3[- (1+i)], end=" ")

######################################
# Q4
######################################


# def fibonacci(num):
#     if num == 0:
#         return 0
#     elif num <= 2:
#         return 1
#     else:
#         return fibonacci(num - 1) + fibonacci(num - 2)
# num = int(input("How many Fibonacci numbers to generate: "))
# print(*list(map(fibonacci, range(num))), sep=" ")

######################################
# Q5
######################################

# def commonElementsInList(a, b):
#     return set(a).intersection(set(b))
#
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# print(commonElementsInList(a, b))


######################################
# Q6
######################################
cowsCount = 0
bullsCount = 0
DIGITSLENGTH = 4
wrong = True
print("Welcome to the Cows and Bulls Game!")
prompt = "Enter a number: "
randomFourDigits = list(str(random.randint(1000,10000)))
print("randomFourDigits", randomFourDigits)

while wrong:
    cowsCount = 0
    bullsCount = 0
    guess = list(str(input(prompt)))
    for i in range(DIGITSLENGTH):
        if randomFourDigits[i] == guess[i]:
            cowsCount += 1
        elif (randomFourDigits[i] != guess[i]) and (guess[i] in set(randomFourDigits)):
            bullsCount += 1
    if cowsCount == DIGITSLENGTH:
        wrong = False
    else:
        print(str(cowsCount) + " cow, "  + str(bullsCount) + " bull")


