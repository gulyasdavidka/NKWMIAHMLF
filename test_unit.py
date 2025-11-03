import pytest
from calculator import Calculator

def test_add():
    calc = Calculator()
    assert calc.add(3, 4) == 7
    assert calc.add(-1, 1) == 0

def test_subtract():
    calc = Calculator()
    assert calc.subtract(10, 5) == 5
    assert calc.subtract(0, 3) == -3

def test_multiply():
    calc = Calculator()
    assert calc.multiply(3, 5) == 15
    assert calc.multiply(-2, 3) == -6

def test_divide():
    calc = Calculator()
    assert calc.divide(10, 2) == 5
    assert calc.divide(-6, 3) == -2

def test_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.divide(5, 0)
