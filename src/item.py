import csv
import os


class InstantiateCSVError(Exception):
    pass


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __add__(self, other):
        """Сложение параметров экземпляров классов по количеству товара"""
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        raise ValueError("Можно складывать только с классом Phone")

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            self.__name = value[0:10]
            return value
        self.__name = value
        return value


    @classmethod
    def instantiate_from_csv(cls, filename):
        """
        Класс-метод открывает файл формата csv
        и создает экземпляр класса
        """
        if os.path.exists(filename):
            Item.all.clear()
            try:
                with open(filename, newline='') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        name = row['name']
                        price = float(row['price'])
                        quantity = int(row['quantity'])
                        cls(name, price, quantity)
            except (KeyError, ValueError):
                raise InstantiateCSVError(f'Файл {filename} поврежден')
        else:
            raise FileNotFoundError(f'Отсутствует файл {filename}')


    @staticmethod
    def string_to_number(number: str):
        """
        Статический метод возвращающий число из числа строки
        """
        return int(float(number))

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name
