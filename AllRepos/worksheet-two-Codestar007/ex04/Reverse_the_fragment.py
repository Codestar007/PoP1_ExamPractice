a = input()
first_h = a.find('h') 
second_h  = a.rfind('h',first_h+1, len(a))
t = a[first_h + 1:second_h]
print(a[:first_h +1] + t[::-1] + a[second_h:])
