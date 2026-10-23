key = input("Enter answer key (for example ABCD): ").upper()
answers = input("Enter student answers; use X if blank: ").upper()

if len(key) != len(answers):
    print("Error: answer strings must have equal length.")
else:
    correct = 0
    incorrect = 0
    unanswered = 0

    for i in range(len(key)):
        if answers[i] == "X":
            unanswered += 1

        elif answers[i] == key[i]:
            correct += 1

        else:
            incorrect += 1

    score = correct - 0.25 * incorrect

    print("Correct:", correct)
    print("Incorrect:", incorrect)
    print("Unanswered:", unanswered)
    print("Final score:", round(score, 2))