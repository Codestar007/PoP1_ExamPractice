# a) The  code saves a count of the occurent of each character.
    #{s:4, a:3, f:1, r:1}
def points():
    return "Points list"

def foo(s):
    d = {}
    for ch in s:
        v = d.get(ch, 0)
        d[ch] = v + 1
    return d
print(foo("sassafras"))

# b)
# ANS:  ['a', 'n', 'd', 'a', 'n', 'd']
def letters(s):
    ss = []
    for ch in s:
        if ch.isalpha():
            ss.append(ch.lower())
    return ss
print(letters("1 and 2 and 3"))

#c)
# ANS: ['andand']
def lets(s):
    return "".join(filter(lambda x: x.isalpha(), list(s)))
print(lets("1 and 2 and 3"))

#d0
# ANS: Calls the "Points" function
def f(n):
    return [foo, points, letters, lets][n]
print(f(1))