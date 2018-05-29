n = int(input())
Y = set() # set of YESs
N = set() # set of NOs
P = {int(i) for i in range(n)}# secrete number range
while True:
    help_requested = input()
    if help_requested != "HELP":
        BG = {int(i) for i in help_requested.split(' ')}
        AA = input()
        if AA == "YES":
            P.intersection_update(BG)
        else:
            N.update(BG)
            P.difference_update(N)
    else:
        result = list(P)
        result.sort()
        print(' '.join(str(i) for i in result))
        break
