transactions = [
    {"id": "T001", "item": "Laptop", "quantity": 1, "price": 1200.00, "category": "Electronics", "customer_id": "C101"},
    {"id": "T002", "item": "Mouse", "quantity": 3, "price": 25.50, "category": "Accessories", "customer_id": "C102"},
    {"id": "T003", "item": "Keyboard", "quantity": 2, "price": 75.00, "category": "Accessories", "customer_id": "C101"},
    {"id": "T004", "item": "Laptop", "quantity": 1, "price": 1200.00, "category": "Electronics", "customer_id": "C103"},
    {"id": "T005", "item": "Webcam", "quantity": 5, "price": 40.00, "category": "Accessories", "customer_id": "C102"}
]

# 1.1 і 1.2 Додаємо нову транзакцію T006
new_transaction = {"id": "T006", "item": "Headphones", "quantity": 2, "price": 50.00, "category": "Accessories", "customer_id": "C104"}
transactions.append(new_transaction)

# 1.3 Знаходимо T003 і змінюємо price на 70.00
for t in transactions:
    if t["id"] == "T003":
        t["price"] = 70.00
        break

# 2.1 Створюємо множину унікальних покупців
unique_customers = set()
for t in transactions:
    unique_customers.add(t["customer_id"])

# 2.2 Створюємо список кортежів (item, price)
item_prices = []
for t in transactions:
    item_prices.append((t["item"], t["price"]))

# 3.1 Підрахунок загальної кількості quantity для категорії "Electronics"
total_electronics_qty = 0
for t in transactions:
    if t["category"] == "Electronics":
        total_electronics_qty += t["quantity"]

# 3.2 Видаляємо транзакцію з ID "T005"
index_to_remove = None
for i, t in enumerate(transactions):
    if t["id"] == "T005":
        index_to_remove = i
        break
if index_to_remove is not None:
    transactions.pop(index_to_remove)

# 4.1 Сортування за ціною (зростання) і виведення перших двох елементів
sorted_by_price = sorted(transactions, key=lambda x: x["price"])
first_two = sorted_by_price[:2]

print("Транзакції після змін:")
for t in transactions:
    print(t)
print("\nУнікальні покупці:", unique_customers)
print("Ціни товарів (товар, ціна):", item_prices)
print("Загальна кількість товарів категорії 'Electronics':", total_electronics_qty)
print("Перші дві транзакції за ціною (за зростанням):")
for t in first_two:
    print(t)