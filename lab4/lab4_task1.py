from typing import List, Dict

class Tovar:
    def __init__(self, name: str, price: float, tags: List[str] = None, specs: Dict[str, str] = None):
        self.name = name
        self.price = float(price)
        self.tags = tags or []
        self.specs = specs or {}

    def apply_discount(self, percent: float) -> None:
        if percent < 0:
            raise ValueError("percent не може бути від'ємним")
        old = self.price
        self.price = round(self.price * (1 - percent / 100), 2)
        print(f"Знижка {percent}% застосована: {old} -> {self.price}")

    def increase_price(self, amount: float) -> None:
        self.price = round(self.price + amount, 2)

    def add_tag(self, tag: str) -> None:
        if tag not in self.tags:
            self.tags.append(tag)

    def remove_tag(self, tag: str) -> None:
        if tag in self.tags:
            self.tags.remove(tag)

    def update_spec(self, key: str, value: str) -> None:
        self.specs[key] = value

    def remove_spec(self, key: str) -> None:
        if key in self.specs:
            del self.specs[key]

    def display_info(self) -> str:
        """Повернути зручний для читання опис товару."""
        lines = [f"Товар: {self.name}", f"Ціна: {self.price} грн"]
        if self.tags:
            lines.append("Теги: " + ", ".join(self.tags))
        if self.specs:
            specs_str = ", ".join(f"{k}: {v}" for k, v in self.specs.items())
            lines.append("Характеристики: " + specs_str)
        return "\n".join(lines)


if __name__ == '__main__':
    p = Tovar(name='Кружка', price=120.0, tags=['кухонне'], specs={'колір': 'білий', 'обсяг': '350ml'})
    print('--- Початковий товар ---')
    print(p.display_info())

    print('\n--- Оновлюємо товар ---')
    p.add_tag('подарунок')
    p.update_spec('матеріал', 'кераміка')
    p.apply_discount(15)
    print(p.display_info())
