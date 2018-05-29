a = input()
first_h, second_h = a.find("h"), a.rfind("h")
x = a[:first_h+1]
y = a[first_h + 1:second_h].replace('h', 'H')
z = a[second_h:len(a)]
print(x + y + z)
