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
