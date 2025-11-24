from lab4_task1 import Tovar

class Elektronika(Tovar):
    def __init__(self, name: str, price: float, tags=None, specs=None, warranty_months: int = 12):
        super().__init__(name, price, tags, specs)
        self.warranty_months = int(warranty_months)

    def extend_warranty(self, months: int):
        if months <= 0:
            raise ValueError("months має бути додатнім")
        old = self.warranty_months
        self.warranty_months += months
        print(f"Гарантію продовжено: {old} міс. -> {self.warranty_months} міс.")

    def display_info(self):
        base = super().display_info()
        return base + f"\nГарантія: {self.warranty_months} міс."


if __name__ == '__main__':
    e = Elektronika('Навушники', 1499.0, tags=['аудіо'], specs={'імпеданс': '32Ω'}, warranty_months=24)
    print('--- Електроніка (перед змінами) ---')
    print(e.display_info())

    print('\n--- Продовжуємо гарантію і змінюємо ціну ---')
    e.extend_warranty(12)
    e.apply_discount(10)
    print(e.display_info())
