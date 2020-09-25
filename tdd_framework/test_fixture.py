import pytest

@pytest.fixture()
def setup():
    print("Executing setup")

def test_test1(setup):
    print("Executing Test1")
    assert True

def test_test2(setup):
    print("Executing Test2")
    assert True

@pytest.fixture()
def setup():
    print("Executing setup")

@pytest.mark.usefixtures("setup")
def test_test1():
    print("Executing Test1")
    assert True
@pytest.mark.usefixtures("setup")
def test_test2():
    print("Executing Test2")
    assert True

# @pytest.fixture(autouse=True)
# def setup():
#     print("Executing setup")
#
# def test_test1():
#     print("Executing Test1")
#     assert True
#
# def test_test2():
#     print("Executing Test2")
#     assert True