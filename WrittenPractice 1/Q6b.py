# Delete negative numbers from the list 3 marks
# Issue - out of index error due to deletion of an entry and listt size change
# Start deletion from the rear

lst = [1, -2, 3, 4, -5,7,8,-9,-12]
for i in range(len(lst)):
    index = len(lst)-(1+i)
    if lst[index] < 0:
        lst.remove(lst[index])
print(lst)