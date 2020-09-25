import pytest

@pytest.fixture()
def setup1():
    print("\nExecuting setup1")
    yield
    print("\nExecuting teardown1")
@pytest.fixture()
def setup2(request):
    print("\nExecuting setup2")
    def teardown_a():
        print("\nExecuting teardown_a")

    def teardown_b():
        print("Executing teardown_b")
    request.addfinalizer(teardown_a)
    request.addfinalizer(teardown_b)

def test1(setup1):
    print("Executing Test1")

def test2(setup2):
    print("Executing Test2")