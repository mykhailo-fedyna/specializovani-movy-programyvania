def format_name(first_name, last_name, upper_case=False):
	full = f"{first_name} {last_name}"
	if upper_case:
		return full.upper()
	return f"{first_name.capitalize()} {last_name.capitalize()}"


if __name__ == "__main__":
	# Виклик 4.1: лише обов'язкові аргументи
	print(format_name("mykhajlo", "fedyna"))

	# Виклик 4.2: змінено дефолтний параметр (upper_case=True)
	print(format_name("mykhajlo", "fedyna", upper_case=True))

