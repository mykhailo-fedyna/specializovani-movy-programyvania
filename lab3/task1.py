# Завдання I: Управління запасами складу

inventory = [
    "Laptop:15",
    "Monitor:25",
    "Keyboard:50",
    "Mouse:45",
    "Webcam:10",
    "Headphones:30",
    "Laptop:5"  # Дублікат товару, але з іншою партією/кількістю
]

print("Початковий список inventory:")
for item in inventory:
    print(" -", item)
print()

# 1. Розділення та нормалізація
processed_inventory = [] 
for record in inventory:
    name = record.split(":")[0]
    processed_inventory.append(name)

print("1. Список назв товарів (нормалізація):")
print(processed_inventory)
print()

# 2. Додавання нових товарів
# 2.1 Додаємо один товар "Speaker"
processed_inventory.append("Speaker")

# 2.2 Додаємо одразу два товари: "Printer" та "Scanner"
processed_inventory.extend(["Printer", "Scanner"]) 

print("2. Після додавання нових товарів:")
print(processed_inventory)
print()

# 3. Перевірка дублікатів та сортування
# 3.1 Порахуємо, скільки разів зустрічається "Laptop"
laptop_count = processed_inventory.count("Laptop")
print(f"3.1 Кількість товарів 'Laptop' у списку: {laptop_count}")

# 3.2 Сортування за алфавітом
processed_inventory.sort()
print("3.2 Відсортований список:")
print(processed_inventory)
print()

# 4. Вилучення товарів
# 4.1 Видалимо перший товар з назвою "Mouse"
if "Mouse" in processed_inventory:
    processed_inventory.remove("Mouse")
    print("4.1 Після видалення 'Mouse':")
    print(processed_inventory)
else:
    print("4.1 'Mouse' не знайдено у списку")
print()

# 4.2 Видалимо товар за індексом 3 (як приклад) за допомогою del
index_to_delete = 3
if 0 <= index_to_delete < len(processed_inventory):
    del processed_inventory[index_to_delete]
    print(f"4.2 Після видалення елемента на позиції {index_to_delete}:")
    print(processed_inventory)
else:
    print(f"4.2 Індекс {index_to_delete} поза діапазоном (0..{len(processed_inventory)-1})")

print() 