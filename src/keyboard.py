from src.item import Item


class MixinLang:
    """
    Класс Mixinlang, добавляющий функционал классу Keyboard
    и передающий дополнительный атрибут language.
    :param name: Название продукта.
    :param price: Цена продукта.
    :param quantity: Количество продукта.
    :param language: Имеет только 2 варианта раскладки языка 'EN', 'RU'.
    По умолчанию вариант 'EN'.
    """

    __slots__ = ('EN', 'RU')

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        self.__language = 'EN'

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        """
        Метод для изменения языка раскладки клавиатуры.
        Изменяет вариант раскладки на второй доступный.
        """
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'


class Keyboard(MixinLang, Item):
    """
    Класс продукта Keyboard, имеющий наследование атрибутов от Item,
    функционала и дополнительного атрибута language от MixinLang.
    """
    pass
