list = [1, -5, 6, 9, 85, 10, 42,-9, 13, 27]
starting = True
for i in range(len(list)):
    if starting == True:
        max = list[i]
        maxIndex = i
        min = list[i]
        minIndex = i
        starting = False

    if list[i] > max:
        max = list[i]
        maxIndex = i
    elif list[i] < min:
        min = list[i]
        minIndex = i

print("Max",max,"Min", min)
list[maxIndex], list[minIndex] = list[minIndex], list[maxIndex]
print(list)