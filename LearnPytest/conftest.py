import pytest


@pytest.fixture(scope="module", autouse=True)
def tc_setUp(browser):
    if browser == "chrome":
        print("launch chrome browser")
    elif browser == "ff":
        print("launch firefox browser")
    elif browser == "edge":
        print("launch firefox browser")
    else:
        print("provide valid browser")
    print("login")
    print("Browse products")
    yield
    print("logoff")
    print("close browser")


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="module", autouse=True)
def browser(request):
    return request.config.getoption("--browser")
