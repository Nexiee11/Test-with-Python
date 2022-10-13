import tz2f
import pytest

data = tz2f.read_from_file('test.txt')

def test_max():
    assert tz2f._max(data) == 4 
def test_min(): 
    assert tz2f._min(data) == 1
def test_sum():
    assert tz2f._sum(data) == 10
def test_mult():
    assert tz2f._mult(data) == 24 
def test_mult_greater_than_sum():
    assert tz2f._mult(data) > tz2f._sum(data) 


