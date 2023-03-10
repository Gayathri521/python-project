import pytest
@pytest.fixture
def setUp():
    print("open Browser")
    print("Login")
    print("Browse the product")
    yield
    print("close the browser")
def test_add(setUp):
    print()
