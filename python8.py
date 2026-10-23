students = ["Asha", "Bala", "Charan"]
subjects = ["Python", "Maths", "English"]

marks = [
    [85, 78, 90],
    [92, 88, 84],
    [76, 95, 80]
]

highest_total = -1
top_student = ""

for i in range(len(students)):
    total = sum(marks[i])
    average = total / len(subjects)

    print(
        students[i],
        "total:", total,
        "average:", round(average, 2)
    )

    if total > highest_total:
        highest_total = total
        top_student = students[i]

for j in range(len(subjects)):
    subject_total = 0

    for i in range(len(students)):
        subject_total += marks[i][j]

    subject_average = subject_total / len(students)

    print(
        subjects[j],
        "average:",
        round(subject_average, 2)
    )

print("Top student:", top_student, "with total", highest_total)