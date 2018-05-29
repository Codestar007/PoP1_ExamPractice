def reverseOrd():
    curr = int(input())
    if curr != 0:
        reverseOrd()
    print(curr)
reverseOrd()
