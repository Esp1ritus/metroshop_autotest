from datetime import datetime

from selenium.webdriver import ActionChains


class Base:
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver)

    def getCurrentURL(self):
        url = self.driver.current_url
        print('Текущая ссылка: ' + url)

    def assert_word(self,word, result):
        assert word == result, 'Значения не совпадают!'
        print('Значения совпадают')

    def assert_url(self,result):
        url = self.driver.current_url
        print(url)
        assert url == result, ('Ссылки не совпадают!')
        print('Ссылки совпадают.')

    def get_screen(self):
        date = datetime.now()
        screen_name = f'{date}.png'
        self.driver.save_screenshot(f'screen/{screen_name}')
        print('Скриншот экрана сохранен')