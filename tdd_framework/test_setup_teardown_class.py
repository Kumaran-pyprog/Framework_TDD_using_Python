class Testclass:
    @classmethod
    def setUp_module(cls):
        print("\nSetUp Module")

    @classmethod
    def teardown_module(cls):
        print("\nTeardown Module")

    def setUp_method(self,method):
        if method == self.test1:
            print("\nSetting up test1")
        elif method == self.test2:
            print("\nSetting up test2")
        else:
            print("\nSetting up unknown test")

    def teardown_function(self,method):
        if method == self.test1:
            print("\nTeardown down test1")
        elif method == self.test2:
            print("\nTeardown down test2")
        else:
            print("\nTeardown down unknown test")

    def test1(self):
        print("Executing test1")
        assert True

    def test2(self):
        print("Executing test2")
        assert True

