import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import *

class MosmetroMainPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    url = 'https://shop.mosmetro.ru/'
    #Locators
    search = '//*[@id="rec299975243"]/div/div/div/div/div/input'
    covers_menu = '//*[@id="nav299975239"]/div/div[3]/nav/ul/li[5]/a'
    cards = '//*[@id="rec414804388"]/div/div/div[2]/div/div[1]/div[2]/a/div/div[2]/div[1]'
    search_results = '//*[@id="rec299975243"]/div/div/div/div[2]/div/div[2]/h3'
        #Getters
    def get_covers_items(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.covers_menu)))
    def get_search_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search)))
    def get_cards_page(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cards)))

    def check_result(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_results)))
    #Actions
    def click_btn(self):
        self.get_covers_items().click()
        print('Кликнули по кнопке Каталога')
    def find_search(self, item):
        self.get_search_field().click()
        self.get_search_field().send_keys(item)
        print('Заполнили поле для поиска')
        self.get_search_field().send_keys(Keys.ENTER)
        print('Подтвердили поиск нажатием Enter')
        page_text = self.check_result().text
        confirm = f'Результаты по запросу: {item}'
        assert confirm == page_text, 'Страница с результатами не открылась!'
        print('Получили результаты поискового запроса на сайте')
        time.sleep(3)
    # Methods
    def getItems(self):
        self.getCurrentURL()
        self.driver.maximize_window()
        time.sleep(2)
        self.get_covers_items().click()
        print('Нажали на пункт "Канцелярия"')
        time.sleep(2)
        self.get_cards_page().click()
        print('Нажали на кнопку')
        time.sleep(2)
        print('Выполнен переход в раздел "Обложки на документы"')