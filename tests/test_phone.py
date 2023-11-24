from src.phone import Phone


def test__repr__():
    phone1 = Phone("Samsung", 40000, 100, 2)
    assert repr(phone1) == "Phone('Samsung', 40000, 100, 2)"


def test__str__():
    phone1 = Phone("Samsung", 40000, 100, 2)
    assert str(phone1) == 'Samsung'


def test__add__phone():
    phone1 = Phone("Samsung", 40000, 100, 2)
    phone2 = Phone("HaiWei", 30000, 80, 1)
    assert phone1 + phone2 == 180


def test_setter():
    phone1 = Phone("Samsung", 40000, 100, 2)
    assert phone1.number_of_sim == 2
    phone1.number_of_sim = 3
    assert repr(phone1) == "Phone('Samsung', 40000, 100, 3)"
