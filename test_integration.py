from calculator import Calculator

def test_combined_operations():
    calc = Calculator()
    # (3 + 5) * 2 - 4 / 2 = 14
    result = calc.subtract(calc.multiply(calc.add(3, 5), 2), calc.divide(4, 2))
    assert result == 14

def test_complex_chain():
    calc = Calculator()
    # ((10 - 2) / 2) + (3 * 2) = 4 + 6 = 10
    result = calc.add(calc.divide(calc.subtract(10, 2), 2), calc.multiply(3, 2))
    assert result == 10
