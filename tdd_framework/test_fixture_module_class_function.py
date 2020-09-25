import pytest

@pytest.fixture(scope="module",autouse=True)
def setupModule2():
    print("\nExecuting setup Module2")

@pytest.fixture(scope="class", autouse=True)
def setupClass2():
    print("\nExecuting setup Class2 ")

@pytest.fixture(scope="function",autouse=True)
def setupFunction2():
    print("\nExecuting setup Function2")

class TestClass:
    def test_1(self):
        print("Executing test_1")
        assert True

    def test_2(self):
        print("Executing test_2")
        assert True
