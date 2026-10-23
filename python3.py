n = int(input("Enter number of examinations (at least 2): "))

if n < 2:
    print("Enter at least two examinations.")
else:
    marks = []
    valid = True

    for i in range(n):
        mark = float(input(
            "Enter mark for exam " + str(i + 1) + ": "
        ))

        if mark < 0 or mark > 100:
            valid = False

        marks.append(mark)

    if not valid:
        print("Invalid mark. Marks must be from 0 to 100.")
    else:
        print("Marks:", marks)

        for i in range(1, n):
            change = marks[i] - marks[i - 1]
            print("Change from exam", i, "to", i + 1, ":", change)

        print("Highest mark:", max(marks))

        if marks[-1] > marks[0]:
            print("Overall trend: Improving")
        elif marks[-1] < marks[0]:
            print("Overall trend: Declining")
        else:
            print("Overall trend: Unchanged")