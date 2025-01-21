import pytest

def method1():
    print("Hello World")

@pytest.mark.smoke # assertion -> good to have, for e.g here we are marking this is a smoke test candidate
def test_method2():
    print("test1")
    assert 1-1 == 2 # test will fail

@pytest.mark.regression
def test_method3():
    print("test2")
    assert 1 + 1 == 2 # test will pass

def test_method4():
    print("Test4")
    assert True == False # test will fail

@pytest.mark.smoke
def test_method5():
    print("Test5")
    assert 5 == 5 # test will pass
