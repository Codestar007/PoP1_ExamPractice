def capitalize(lower_case_word):
    cap = chr(ord(lower_case_word[0]) - 32) + lower_case_word[1:]
    return cap

line = input().split(' ')
for word in line:
    if word[0].islower:
        print(capitalize(word), end = ' ')
    else:
        print(word)