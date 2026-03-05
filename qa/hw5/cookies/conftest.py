import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    drv = webdriver.Chrome(options=options)
    drv.implicitly_wait(10)
    yield drv
    drv.quit()