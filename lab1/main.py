# Завдання 1: Сума парних чисел у діапазоні
print("Task 1: Sum of even numbers in a range")
var_start = 1
var_end = 20 

total_sum = 0
for num in range(var_start, var_end + 1):
	if num % 2 == 0:
		total_sum += num

print(f"The sum of even numbers in the range from {var_start} to {var_end}: {total_sum}")

#########################################

# Завдання 2: Добуток всіх непарних чисел у діапазоні
print("\nTask 2: Product of all odd numbers in a range")
var_start = 1 
var_end = 10 
var_step = 1 

total_mult = 1
for num in range(var_start, var_end + 1, var_step):
    if num % 2 != 0:
        total_mult *= num

print(f"The product of all odd numbers in the range from {var_start} to {var_end}: {total_mult}")

#########################################

# Завдання 3: Визначення категорії товару за ціною
print("\nTask 3: Determining product category by price")
product_name = "Laptop"
price = 750

if price <= 500:
	category = 'Budget'
elif 501 <= price <= 1000:
	category = 'Standard'
else:
	category = 'Premium'

print(f"Product: {product_name}")
print(f"Price: {price}")
print(f"Category: {category}")

#########################################

# Завдання 4: Визначення придатності студента до стипендії
print("\nTask 4: Determining student's eligibility for a scholarship")
def check_scholarship(gpa, is_active_in_student_council, has_volunteer_experience):
	if gpa >= 4.5 and is_active_in_student_council:
		scholarship_type = 'full'
	elif gpa >= 4.0 or has_volunteer_experience:
		scholarship_type = 'partial'
	elif not (gpa >= 4.5 and is_active_in_student_council) and not (gpa >= 4.0 or has_volunteer_experience):
		scholarship_type = 'no'
	else:
		scholarship_type = 'no'
	return scholarship_type

test_cases = [
	{"gpa": 4.7, "is_active_in_student_council": True, "has_volunteer_experience": False},   # full
	{"gpa": 4.2, "is_active_in_student_council": False, "has_volunteer_experience": True},   # partial
	{"gpa": 3.8, "is_active_in_student_council": False, "has_volunteer_experience": False},  # no
]

for i, case in enumerate(test_cases, 1):
	result = check_scholarship(case["gpa"], case["is_active_in_student_council"], case["has_volunteer_experience"])
	print(f"Test {i}: GPA={case['gpa']}, Active={case['is_active_in_student_council']}, Volunteer={case['has_volunteer_experience']} => Scholarship: {result}")

##########################################

# Завдання 5: Складні обчислення з використанням циклів та умов
print("\nTask 5: Complex calculations using loops and conditions")
var_start = 1
var_end = 10

total_result = 0

for num in range(var_start, var_end + 1):
    if num % 3 == 0 or num % 5 == 0:
        continue
    if num % 2 == 0:
        total_result += num ** 2
        print(f"Current number: {num}, Intermediate total_result: {total_result}")
    else:
        total_result -= num
        print(f"Current number: {num}, Intermediate total_result: {total_result}")

print("Final value total_result:", total_result)

##########################################

# Завдання 6: Пошук першого числа, що ділиться на 7 у діапазоні
print("\nTask 6: Find first number divisible by 7 in range")

# Випадок 1: у діапазоні є число, що ділиться на 7
var_start = 10
var_end = 30
found = False
for num in range(var_start, var_end + 1):
	if num % 7 == 0:
		print(f"First number divisible by 7 in range {var_start}-{var_end}: {num}")
		found = True
		break
if not found:
	print(f"No number divisible by 7 found in range {var_start}-{var_end}")

# Випадок 2: у діапазоні немає числа, що ділиться на 7
var_start = 8
var_end = 13
found = False
for num in range(var_start, var_end + 1):
	if num % 7 == 0:
		print(f"First number divisible by 7 in range {var_start}-{var_end}: {num}")
		found = True
		break
if not found:
	print(f"No number divisible by 7 found in range {var_start}-{var_end}")
	
# Завдання 7: Пошук "щасливого" числа у діапазоні
print("\nTask 7: Find 'happy' number in range")
start_number = int(input("Enter range start: "))
end_number = int(input("Enter range end: "))

found = False
current = start_number
while current <= end_number:
	if current % 2 == 0: 
		if current % 7 == 0 and current % 3 != 0:
			print(f"Happy number find: {current}")
			found = True
			break
	current += 1

if not found:
	print("There is no 'lucky' number in the selected range.")
	
##########################################