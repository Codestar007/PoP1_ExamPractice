n =4
theString = "and and you me print printout languages the and number of and andy me languages"
listOfWords = theString.split(" ")
mydict = dict()
for i in range(len(listOfWords)):
    value = mydict.get(listOfWords[i], 0)
    mydict[listOfWords[i]] = value + 1

# SORT
print(sorted(mydict))
print(mydict)




