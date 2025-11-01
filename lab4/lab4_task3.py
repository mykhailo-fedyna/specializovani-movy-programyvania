from lab4_task2 import Elektronika

class Manufacturer:
    def __init__(self, name: str, country: str, contact: str = ''):
        self.name = name
        self.country = country
        self.contact = contact

    def full_info(self) -> str:
        contact_part = f", контакт: {self.contact}" if self.contact else ''
        return f"{self.name} ({self.country}){contact_part}"

    def is_local(self, country: str) -> bool:
        return self.country.lower() == country.lower()


class ElektronikaWithManufacturer(Elektronika):
    def __init__(self, name: str, price: float, manufacturer: Manufacturer, tags=None, specs=None, warranty_months: int = 12):
        super().__init__(name, price, tags, specs, warranty_months)
        self.manufacturer = manufacturer

    def show_manufacturer(self) -> str:
        return self.manufacturer.full_info()

    def display_info(self) -> str:
        base = super().display_info()
        return base + f"\nВиробник: {self.show_manufacturer()}"


if __name__ == '__main__':
    m = Manufacturer('Acme Electronics', 'Україна', contact='+380501112233')
    ew = ElektronikaWithManufacturer('Портативна колонка', 2399.0, manufacturer=m, tags=['аудіо', 'портативне'], specs={'потужність': '10W'}, warranty_months=18)

    print('--- Електроніка з виробником ---')
    print(ew.display_info())

    print('\n--- Перевіряємо локальність виробника ---')
    print('Виробник локальний?', ew.manufacturer.is_local('Україна'))
