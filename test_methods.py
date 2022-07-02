import pytest
import math

@pytest.mark.tc1
@pytest.mark.sanity
def test_add():
    assert 3+3 == 9

@pytest.mark.tc2
@pytest.mark.smoke
def test_sub():
    assert 5-3 == 2

@pytest.mark.smoke
def test_mul():
    assert 5*3 == 15

def test_div():
    assert 20/4 == 6

def test_sqrt():
    num = 25
    print(45465656545)
    assert math.sqrt(num) == 5

@pytest.mark.regression
def test_sqrt1():
    num = 7
    assert math.sqrt(num) == 7

@pytest.mark.tc4
@pytest.mark.regression
def test_new_mehtod():
    assert 1 == 2, 'numbers are not equal'