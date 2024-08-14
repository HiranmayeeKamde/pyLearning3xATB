import pytest
class Test:
    @pytest.fixture(scope="function", autouse=True)
    def myfixture(self):
        print("My fixture is called")
    def mytest_method1(self):
        print("Method -1 is called")

    def mytest_method2(self):
        print("Method -2 is called")


# obj = Test()
# obj.mytest_method1()