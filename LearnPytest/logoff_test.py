import pytest

@pytest.mark.skip
def testLogin():
    print("login successfully")

def testlogoff():
    print("login off successfully")

@pytest.mark.sanity
def testcalculation():
    assert 2+2 == 4

@pytest.mark.xfail
def testcalculation1():
    assert 2+2 == 4