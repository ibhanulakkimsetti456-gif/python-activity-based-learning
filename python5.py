n = int(input("Enter number of transactions: "))
threshold = float(input("Enter suspicious amount threshold: "))

ids = []
amounts = []

for i in range(n):
    transaction_id = input("Enter transaction ID: ")
    amount = float(input("Enter transaction amount: "))

    ids.append(transaction_id)
    amounts.append(amount)

found = False

for i in range(n):
    reasons = []

    if ids[i] in ids[:i]:
        reasons.append("duplicate ID")

    if amounts[i] > threshold:
        reasons.append("amount above threshold")

    if reasons:
        found = True
        print(
            "Suspicious transaction:",
            ids[i],
            amounts[i],
            "-",
            ", ".join(reasons)
        )

if not found:
    print("No suspicious transactions found.")