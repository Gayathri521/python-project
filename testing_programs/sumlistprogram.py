import pytest
def find_sum(l):
    s=0
    for i in l:
        s+=i
    return s
@pytest.mark.parametrize("l,expected_output", [([10,20],30),([1.8,5.0],6.8)])
def test(l,expected_output):
    assert find_sum(l) == expected_output

