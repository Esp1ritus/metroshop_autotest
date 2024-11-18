import time
import pytest
from selenium import webdriver


@pytest.fixture()
def set_up():
    print("\nЗапуск теста")
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    options = webdriver.ChromeOptions()
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument("--enable-javascript")
    driver = webdriver.Chrome(options=options)
    url = 'https://shop.mosmetro.ru/'
    driver.get(url)
    driver.maximize_window()
    time.sleep(3)
    yield driver

    print("\nТест завершен!")
    driver.quit()

@pytest.fixture(scope='module')
def set_group():
    print("Enter system")
    yield
    print("Exit system")