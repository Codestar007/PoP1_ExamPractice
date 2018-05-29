students = int(input())
lang_spoken_by_all = set()
spoken_by_at_least_1 = set()
student_speaks = set()

for i in range(students):
    for j in range(int(input())):
        student_speaks.add(input())
    if len(lang_spoken_by_all) == 0:
        lang_spoken_by_all = student_speaks
        spoken_by_at_least_1 = spoken_by_at_least_1.union(student_speaks)
        student_speaks = set()
    else:
        lang_spoken_by_all = lang_spoken_by_all.intersection(student_speaks)
        spoken_by_at_least_1 = spoken_by_at_least_1.union(student_speaks)
        student_speaks = set()
print(len(lang_spoken_by_all))
for num in sorted(lang_spoken_by_all):
    print(num)
print(len(spoken_by_at_least_1))
for lang in sorted(spoken_by_at_least_1):
    print(lang)

