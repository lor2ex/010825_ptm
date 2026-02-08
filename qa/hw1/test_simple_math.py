import pytest
from simple_math import SimpleMath


@pytest.fixture
def simple_math():
    return SimpleMath()

def test_square(simple_math):
    assert simple_math.square(2) == 4
    assert simple_math.square(-3) == 9
    assert simple_math.square(0) == 0

def test_cube(simple_math):
    assert simple_math.cube(2) == 8
    assert simple_math.cube(-3) == -27
    assert simple_math.cube(0) == 0
