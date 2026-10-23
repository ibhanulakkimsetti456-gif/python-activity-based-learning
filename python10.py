days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

prepared = [100, 120, 90, 110, 80]
served = [92, 100, 86, 95, 70]

threshold = 10

for i in range(len(days)):

    if (prepared[i] <= 0 or served[i] < 0
            or served[i] > prepared[i]):
        print(days[i], "- invalid data")

    else:
        leftovers = prepared[i] - served[i]
        waste_percent = leftovers / prepared[i] * 100

        print(
            days[i],
            "leftovers:", leftovers,
            "waste:", round(waste_percent, 2), "%"
        )

        if waste_percent > threshold:
            print("Warning: waste exceeds", threshold, "%")