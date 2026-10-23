products = [
    ("P101", 25.0, 10),
    ("P102", 80.0, 3),
    ("P103", 12.5, 0),
    ("P104", 40.0, 7)
]

total_value = 0

for product in products:
    product_id, price, quantity = product

    if price < 0 or quantity < 0:
        print("Invalid record:", product_id)

    else:
        value = price * quantity
        total_value += value

        print(product_id, "inventory value:", value)

        if quantity < 5:
            print("Replenishment required for", product_id)

print("Total catalogue inventory value:", round(total_value, 2))