import pytest
class TestSamplePy:
    def test_anagram(self):
        str1 = 'madam'
        str2 = 'madam'
        ang1 = list(str1)
        res1 = ang1.sort()
        print("res1:", res1)
        ang2 = list(str2)
        res2 = ang2.sort()
        print("res2:", res2)
        assert res1 == res2

    def test_reversestring(self):
        str1="malayalam"
        res=str1[::-1]
        assert res==str1

    def test_factorial(self):
        num=5
        fact = 1
        for i in range(1,num+1):
            fact=fact*i
        assert fact==120

    def test_map(self):
        res=list(map(lambda x:x%2==0,[1,2,3,4,5,6]))
        assert res==[0, 1, 0, 1, 0, 1]

    def test_filter(self):
        res=list(filter(lambda x:x%2,[1,2,3,4,5,6]))
        assert res==[1,3,5]

    def test_reduce(self):
        from functools import reduce
        res=reduce((lambda x,y:x*y),[1,2,3,4,5])
        assert res==120

