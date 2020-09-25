from unittest import TestCase
#Production code
def str_len(str):
    return len(str)

#UnitTest
class TestStringlen(TestCase):
    def test_str_len(self):
        str = 'Ashok'
        res = str_len(str)
        assert res == 5

