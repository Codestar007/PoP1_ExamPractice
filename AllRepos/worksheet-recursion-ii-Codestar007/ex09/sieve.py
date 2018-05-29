from math import sqrt

def sieve(n):
    lst = [int(x) for x in range(2, n+1)]
    i = 2
    def helper(i, lst):
        if i + i > n:
            return lst
        else:
            for j in range(2, n+1):
                try:
                    lst.remove(i * j)
                except IndexError:
                    pass
                except ValueError:
                    pass
            t = lst.index(i)
            return helper(lst[t + 1], lst)
    return helper(i, lst)

#print(sieve(10))
