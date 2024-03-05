import pytest
from math_functions import sum, mul, div, sub

def test_sum():
    assert sum(2, 3) == 5
    assert sum(-1, 1) == 0
    assert sum(-1, -1) == -2
    assert sum(0, 0) == 0

def test_mul():
    assert mul(2, 3) == 6
    assert mul(-1, 1) == -1
    assert mul(-1, -1) == 1
    assert mul(0, 1) == 0

def test_div():
    assert div(6, 3) == 2
    assert div(-2, 1) == -2
    assert div(-2, -1) == 2
    with pytest.raises(ZeroDivisionError):
        div(1, 0)

def test_sub():
    assert sub(5, 3) == 2
    assert sub(-1, 1) == -2
    assert sub(-1, -1) == 0
    assert sub(0, 0) == 0
