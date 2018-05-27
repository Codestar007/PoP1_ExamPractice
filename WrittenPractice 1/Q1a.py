listColumn = [c for c in range(1,11)]
listRow = [r for r in range(1,6)]

for i in range(len(listRow)):
	print()
	for j in range(len(listColumn)):
		print(listRow[i] * listColumn[j], end=' ')


#### OR

columnMax = 11
rowMax = 6

for i in range(1,rowMax):
	print()
	for j in range(1,columnMax):
		print(i * j, end=' ')