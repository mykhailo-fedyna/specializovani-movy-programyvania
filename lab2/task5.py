def create_profile(login, password, separator = "| ", **user_data):
	parts = [f"login{separator}{login}", f"password{separator}{password}"]
	for key, value in user_data.items():
		parts.append(f"{key}{separator}{value}")
	return "\n".join(parts)


if __name__ == "__main__":
	my_profile = create_profile("Student", "PI-21", separator = ": ", name='Ivan', age=30,  occupation='Developer', city='Lviv')
	print(my_profile)

