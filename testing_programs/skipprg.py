import pytest
@pytest.mark.hcl
def test_d1():
    assert 10+20==30
def test_d2():
    assert 10-5==5
@pytest.mark.hcl
def test_d3():
    assert 10*5==50
def test_d4():
    assert 10/5==2