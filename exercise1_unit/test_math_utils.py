import math
import pytest
from math_utils import add, div, clamp
import numpy as np

# === Testing Add ===
def test_add_basic():
    assert add(5, 10) == 15

@pytest.mark.parametrize("a,b,expected", [
    (500, 1000, 1500),
    (0, 1000, 1000),
    (-100, 100, 0),
    (-100, -1100, -1200),
])
def test_add_more(a,b,expected):
    assert add(a,b) == expected

# TODO: test if A+B = B+A
def test_add_commutative():
    for a,b in [(1,2), (100,200), (-5,5), (-10,-20)]:
        assert add(a,b) == add(b,a)

# TODO: fix add to reject non-numeric types
def test_add_rejects_non_numeric():
    with pytest.raises(TypeError):
        add("2", "3")
    with pytest.raises(TypeError):
        add([1], [2])
    with pytest.raises(TypeError):
        add(True, 1)

# === Testing Div ===
def test_div_normal():
    assert div(9, 3) == 3

def test_div_raises_on_zero():
    with pytest.raises(ValueError):
        div(1, 0)

def test_div_precision_contract_is_float64_like():
    """
    Contract: div(1, 3) should be ~float64-precise. If someone switches to float32
    (e.g., via NumPy), this tight tolerance will catch it.
    """
    res = div(1.0, 3.0)
    # float64 has ~1e-16 epsilon; this 1e-12 guard will FAIL for float32 (~1e-8 off)
    assert abs(res - (1/3)) < 1e-12

# TODO: test div with floats
def test_div_floats():
    assert div(1.5, 0.5) == 3.0

# TODO: test div with non-infinite denominator 
def test_div_rejects_nonfinite_denominator():
    for bad in (math.inf, -math.inf, math.nan):
        with pytest.raises(ValueError):
            div(1.0, bad)

# === Testing Clamp ===
@pytest.mark.parametrize("x,lo,hi,expected", [
    (5, 0, 10, 5),
    (-1, 0, 10, 0),
    (11, 0, 10, 10),
])
def test_clamp(x,lo,hi,expected):
    assert clamp(x, lo, hi) == expected

def test_clamp_bad_range():
    with pytest.raises(ValueError):
        clamp(1, 5, 4)

# TODO: fix clamp to reject nan values
def test_clamp_rejects_nan():
    with pytest.raises(ValueError):
        clamp(math.nan, 0, 10)
    with pytest.raises(ValueError):
        clamp(5, math.nan, 10)
    with pytest.raises(ValueError):
        clamp(5, 0, math.nan)

# TODO: fix clamp to reject infinite values
def test_clamp_rejects_infinities():
    for bad in (math.inf, -math.inf):
        with pytest.raises(ValueError):
            clamp(bad, 0, 10)
        with pytest.raises(ValueError):
            clamp(5, bad, 10)
        with pytest.raises(ValueError):
            clamp(5, 0, bad)
