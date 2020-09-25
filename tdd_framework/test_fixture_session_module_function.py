import pytest

@pytest.fixture(scope="session",autouse=True)
def setupSession():
    print("\nExecuting setup session 1")

@pytest.fixture(scope="module", autouse=True)
def setupModule():
    print("\nExecuting setup module ")

@pytest.fixture(scope="function",autouse=True)
def setupFunction():
    print("\nExecuting setup Function")

def test1():
    print("Executing test1")
    assert True

def test2():
    print("Executing test2")
    assert True
