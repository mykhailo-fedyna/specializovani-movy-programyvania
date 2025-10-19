employees = {
	"E101": {"name": "Alice Johnson", "department": "Marketing", "salary": 65000,
			 "skills": ["SEO", "Content_Creation"]},
	"E102": {"name": "Bob Smith", "department": "IT", "salary": 85000,
			 "skills": ["Python", "Databases", "Networking"]},
	"E103": {"name": "Charlie Brown", "department": "Marketing", "salary": 70000,
			 "skills": ["Social_Media", "Analytics"]},
	"E104": {"name": "Diana Prince", "department": "IT", "salary": 92000,
			 "skills": ["Cloud", "Python", "Security"]}
}

# 1. Додавання та оновлення даних
# 1.1 Додати E105
employees["E105"] = {
	"name": "Eve Adams",
	"department": "Finance",
	"salary": 75000,
	"skills": ["Budgeting", "Reporting"]
}

# 1.2 Змінити department для E102
employees["E102"]["department"] = "Development"

# 1.3 Збільшити зарплату для E104 на 5000
employees["E104"]["salary"] += 5000

# 2. Аналіз унікальних значень
# 2.1 Унікальні відділи
all_departments = set(emp["department"] for emp in employees.values())

# 2.2 Унікальні навички
core_skills = set()
for emp in employees.values():
	core_skills.update(emp.get("skills", []))

# 3. Видалення та фільтрація
# 3.1 Видалити E103
employees.pop("E103", None)

# 3.2 Список high_earners (name, salary) для salary > 80000
high_earners = [(emp["name"], emp["salary"]) for emp in employees.values() if emp["salary"] > 80000]

# 4. Сортування та відображення
# 4.1 Список ID, відсортованих за ім'ям
sorted_by_name = sorted(employees.keys(), key=lambda eid: employees[eid]["name"])

print("Відсортовано за ім'ям:", sorted_by_name)

# 4.2 Порахуємо співробітників у кожному відділі
dept_counts = {}
for emp in employees.values():
	dept = emp["department"]
	dept_counts[dept] = dept_counts.get(dept, 0) + 1

print("\nКількість співробітників по відділах:")
for dept, count in dept_counts.items():
	print(f"{dept}: {count}")

print("\nУсі відділи:", all_departments)
print("Основні навички:", core_skills)
print("Співробітники з високою зарплатою:", high_earners)