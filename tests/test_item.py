from src.item import Item

"""Здесь надо написать тесты с использованием pytest для модуля item."""


def test_calculate_total_price():
    item1 = Item('1', 100, 10)
    assert item1.calculate_total_price() == 1000


def test_name():
    assert 'Василий' == 'Василий'


def test_string_to_number():
    assert Item.string_to_number('2.75') == 2
    assert Item.string_to_number('2.01') == 2
