import pytest


@pytest.mark.sanity
def testLogin():
    print("login successfully")


def testlogoff():
    print("login off successfully")


def testcalculation():
    assert 2 + 2 == 4