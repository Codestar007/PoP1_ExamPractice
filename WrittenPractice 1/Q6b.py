# Delete negative numbers from the list 3 marks
# Issue - out of index error due to deletion of an entry

lst = [1, -2, 3, 4, -5,7,8,-9,-12]
for i in range(len(lst)):
    if lst[len(lst)-(1+i)] < 0:
        lst.remove(lst[len(lst)-(1+i)])
print(lst)