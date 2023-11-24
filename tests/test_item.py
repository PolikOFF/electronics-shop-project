import csv

from src.item import Item

"""Здесь надо написать тесты с использованием pytest для модуля item."""


def test_calculate_total_price():
    item1 = Item('1', 100, 10)
    assert item1.calculate_total_price() == 1000


def test_string_to_number():
    assert Item.string_to_number('2.75') == 2
    assert Item.string_to_number('2.01') == 2


def test_name():
    item1 = Item("Буковки", 10, 2)
    assert item1.name == "Буковки"
    item1.name = "Слишкоммногобукавок"
    assert item1.name == "Слишкоммно"


def test_instantiate_from_csv():
    Item.instantiate_from_csv('test.csv')
    assert len(Item.all) == 5


def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'


def test__add__():
    item1 = Item("Веб-камера", 9000, 10)
    item2 = Item("Микрофон", 6000, 30)
    assert item1 + item2 == 40
