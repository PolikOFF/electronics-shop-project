from src.keyboard import Keyboard


def test_keyboard():
    keyboard1 = Keyboard('test', 100, 10)
    assert keyboard1.language == 'EN'


def test_change_lang():
    keyboard1 = Keyboard('test', 100, 10)
    keyboard1.change_lang() == 'RU'
    keyboard1.change_lang() == 'EN'
