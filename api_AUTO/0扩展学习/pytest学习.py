import pytest

class TestClass:
    def setup_class(self):
        print('------start')

    def teardown_class(self):
        print('------end')

    def testone(self):
        print('testaaaa')

    def testtwo(self):
        print('testbbbb')


if __name__=='__main__':
    pytest.main(['-s','-v','-x','pytest学习.py'])