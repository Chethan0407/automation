#he conftest.py file in a pytest project is a special module where you can define fixtures, hooks,
# and other configurations that are shared across multiple test files.


from selenium import webdriver
import pytest
@pytest.fixture()
def setup(request):
    global driver
    browser_type = request.config.getoption("--browser")

    if browser_type == "chrome":
        driver = webdriver.Chrome()

    elif browser_type == "firefox":
        driver = webdriver.Firefox()
    return driver



def pytest_addoption(parser):
    parser.addoption( "--browser")







