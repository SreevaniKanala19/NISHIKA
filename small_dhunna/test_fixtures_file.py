import pytest
import pdb

@pytest.fixture
def input_value():
    pdb.set_trace()
    input = 39
    yield
    print(35435435435435435)

@pytest.mark.nishi
def test_divisible_by_3(input_value):
   print(1222222222)
   assert 1 == 1

def test_divisible_by_6(input_value):
   assert input_value % 6 == 0