def readRecord():
    recordFile = open("phonebills.txt", "r")
    thisRecord = recordFile.readline().strip.split(" ")
    

def printOutput():
    pass

def computePhoneBill(accountNum, surname, accBalance, serviceType, callMinutes, offPeakMinute=0):
    initialCost = 0.00
    if serviceType == "R":
        if callMinutes <= 50:
            return callMinutes * 10.00
        else:
            return ((callMinutes - 50) * 20.00) + (50 * 10.00)
    else:
        return 0.00

print(computePhoneBill("A9845", "Hurley", 50.75,"R",60 ))
