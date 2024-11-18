import pytest


# @pytest.fixture(params=["a", "b"])
# def demo_Fixture(request):
#       print(request.param)

@pytest.mark.parametrize("a,b,final", [(2, 6, 8), (5, 8, 15), (5, 10, 15)])
def testLogin(a, b, final):
    assert a + b == final


# @pytest.mark.parametrize("x,y,f", [(2, 6, 8), (5, 8, 13), (5, 10, 15)])
# def testlogoff(x, y, f):
#     assert x + y == f

# def testcalculation():
#     assert 2+2 == 4
