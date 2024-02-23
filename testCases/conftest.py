import pytest
from selenium import webdriver
from utilities.readProperties import ReadConfig

url = ReadConfig.getShopURL()


@pytest.fixture()
def openBrowser(request):
    browser = request.config.getoption("--browser")
    if browser == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.close()



