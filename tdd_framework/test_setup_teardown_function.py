def setUp_module(module):
    print("\nSetUp Module")

def teardown_module(module):
    print("\nTeardown Module")

def setUp_function(function):
    if function == test1:
        print("\nSetting up test1")
    elif function == test2:
        print("\nSetting up test2")
    else:
        print("\nSetting up unknown test")

def teardown_function(function):
    if function == test1:
        print("\nTeardown down test1")
    elif function == test2:
        print("\nTeardown down test2")
    else:
        print("\nTeardown down unknown test")

def test1():
    print("Executing test1")
    assert True

def test2():
    print("Executing test2")
    assert True



