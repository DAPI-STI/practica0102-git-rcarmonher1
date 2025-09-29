from src.math_ops import add

def test_add_enteros():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_add_flotantes():
    assert add(2.5, 0.5) == 3.0
