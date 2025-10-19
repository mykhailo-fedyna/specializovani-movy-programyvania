# Завдання IV: Управління проєктами та завданнями

def main():
	projects = {
		"Web_Redesign": ["Develop_Wireframes", "Design_Mockups", "Implement_Frontend", "Test_UX"],
		"Data_Migration": ["Extract_Legacy_Data", "Clean_Data", "Transform_Data", "Load_New_DB"],
		"Marketing_Campaign": ["Define_Audience", "Create_Content", "Schedule_Posts", "Analyze_Metrics"],
	}

	# 1. Додавання та вставка нових завдань
	# 1.1 Додати новий проєкт "Mobile_App"
	projects["Mobile_App"] = ["Setup_Environment", "Develop_Backend"]

	# 1.2 Для "Web_Redesign" додати "Deploy_Server" в кінець
	projects["Web_Redesign"].append("Deploy_Server")

	# 1.3 Для "Data_Migration" вставити "Backup_Original_Data" на початок
	projects["Data_Migration"].insert(0, "Backup_Original_Data")

	# 2. Об'єднання та аналіз статусу 
	# 2.1 Створити список all_tasks_flat з усіх завдань
	all_tasks_flat = []
	for task_list in projects.values():
		all_tasks_flat.extend(task_list)

	print("Всі завдання (згладжено):", all_tasks_flat)

	# 2.2 Перевірити, чи є дублікати між проєктами
	has_duplicates = len(all_tasks_flat) != len(set(all_tasks_flat))
	print("Чи є дублікати завдань між проєктами?", has_duplicates)

	# 3. Вилучення та підрахунок
	# 3.1 Для "Marketing_Campaign" видалити останнє завдання і вивести його
	removed = projects["Marketing_Campaign"].pop()
	print("Видалено з Marketing_Campaign:", removed)

	# 3.2 Для "Data_Migration" видалити "Clean_Data" за значенням
	if "Clean_Data" in projects["Data_Migration"]:
		projects["Data_Migration"].remove("Clean_Data")
		print('"Clean_Data" видалено з Data_Migration')
	else:
		print('"Clean_Data" не знайдено в Data_Migration')

	# 3.3 Видалити весь проект "Mobile_App"
	projects.pop("Mobile_App", None)
	print('Проєкт "Mobile_App" видалено')

	# 4. Сортування та перейменування (Кортежі)
	# 4.1 Створити список кортежів (кількість_завдань, назва_проєкту), відсортувати за кількістю завдань спаданням
	sorted_projects = sorted(((len(tasks), name) for name, tasks in projects.items()), reverse=True)
	print("Відсортовані проєкти (за кількістю завдань, спадання):", sorted_projects)

	# 4.2 Перейменувати "Test_UX" -> "Final_UX_Review" в "Web_Redesign"
	wr_tasks = projects.get("Web_Redesign", [])
	for i, t in enumerate(wr_tasks):
		if t == "Test_UX":
			wr_tasks[i] = "Final_UX_Review"
			print('"Test_UX" перейменовано на "Final_UX_Review" у Web_Redesign')
			break

	print("\nКінцевий стан проєктів:")
	for name, tasks in projects.items():
		print(f"- {name}: {tasks}")


if __name__ == "__main__":
	main()

