def pascal_tgl(row, column):
    if (column == 0) or (column == row): #base case
        return 1
    else:
        return pascal_tgl(row - 1, column - 1) + pascal_tgl(row - 1, column)

n = 6
for r in range(n):
    therow = ""
    for c in range(r + 1):
        therow = therow + "\t" + str(pascal_tgl(r, c)) +  "\t"
    print((" \t" * (n-r)) + therow)
