def negativeNumber(myList):
    for i in range(len(myList)):
        if myList[i] < 0:
            return myList[i]
    return None

myList = [1,2,5,3,-6,7,12]
#myList = [1,2,5,3,6,7,12]

print(negativeNumber(myList))
