def create_shopping_list(store_name, *items):
	header = f"{store_name}"
	lines = []
	for i, item in enumerate(items, 1):
		lines.append(f"{i}. {item}")
	shopping_list = "\n".join(lines)
	return header, shopping_list


if __name__ == "__main__":
	header, shopping_list = create_shopping_list("MegaMarket", "milk", "bread", "cheese", "apples")

	print(header, shopping_list, sep="\n---\n")
