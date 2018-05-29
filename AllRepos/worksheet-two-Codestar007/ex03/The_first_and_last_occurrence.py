a = input()
first_f = a.find('f') 
second_f  = a.rfind('f',first_f+1, len(a))

if first_f != -1 and second_f != -1:
    print(first_f, second_f)
elif first_f != -1 and second_f == -1:
    print(first_f)
