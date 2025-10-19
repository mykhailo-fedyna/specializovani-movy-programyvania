# Просте рішення завдання II: Аналіз оцінок студентів

# Початковий список (оригінал не модифікую для кроку 4)
orig_grades = [92, 78, 85, 92, 63, 100, 88, 78, 95, 81, 78]
# Створюю робочу копію, щоб змінювати її в кроках 1-3
grades = orig_grades.copy()

print("Початкові оцінки:", orig_grades)
print('---')

# 1. Додавання та вставка
# 1.1 Додаємо 75 в кінець
grades.append(75)
# 1.2 Вставляємо 100 на другу позицію
grades.insert(1, 100)
print("1. Після додавання та вставки:", grades)
print('---')

# 2. Підрахунок та видалення за значенням
# 2.1 Скільки студентів отримали 78
count_78 = grades.count(78)
print(f"2.1 Кількість оцінок 78: {count_78}")
# 2.2 Видаляємо тільки один випадок 92 
grades.remove(92) 
print("2.2 Після видалення одного 92:", grades)
print('---')

# 3. Умовний аналіз та видалення за індексом
# 3.1 Створюємо список high_grades з оцінок >= 90
high_grades = []
for g in grades:
    if g >= 90:
        high_grades.append(g)
print("3.1 Оцінки >= 90:", high_grades)
# 3.2 Зі списку grades видаляємо найнижчу оцінку і виводимо її
min_value = min(grades)
min_index = grades.index(min_value)
removed = grades.pop(min_index)
print(f"3.2 Видалена найнижча оцінка: {removed}")
print("Після видалення найнижчої:", grades)
print('---')

# 4. Сортування та зрізи
# 4.1 Створюємо top_three з трьома найвищими оцінками
top_three = sorted(orig_grades, reverse=True)[:3]
print("4.1 Три найвищі оцінки (top_three):", top_three)
print('---')

