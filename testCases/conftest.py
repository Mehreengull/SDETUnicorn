import pytest
from selenium import webdriver
from utilities.readProperties import ReadConfig

url = ReadConfig.getShopURL()


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def openBrowser(request):
    browser = request.config.getoption("--browser")
    if browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Safari()
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.close()

