n = int(input())

students = []
for _ in range(n):
    students.append(list(map(str, input().split())))

students = sorted(students, key=lambda x: ((-int(x[1])), int(x[2]), (-int(x[3]), x[0])))

for student in students:
    print(student[0])