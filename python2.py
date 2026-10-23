balance = float(input("Enter opening balance: "))
deposits = 0
withdrawals = 0

if balance < 0:
    print("Opening balance cannot be negative.")
else:
    while True:
        kind = input(
            "Enter D-deposit, W-withdrawal, Q-quit: "
        ).upper()

        if kind == "Q":
            break

        if kind != "D" and kind != "W":
            print("Invalid transaction type")
            continue

        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Amount must be positive")

        elif kind == "D":
            balance += amount
            deposits += 1
            print("Deposit successful")

        elif amount <= balance:
            balance -= amount
            withdrawals += 1
            print("Withdrawal successful")

        else:
            print("Insufficient balance")

    print("Final balance:", round(balance, 2))
    print("Successful deposits:", deposits)
    print("Successful withdrawals:", withdrawals)