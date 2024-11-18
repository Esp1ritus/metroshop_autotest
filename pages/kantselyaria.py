import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import *

#наследуем класс Base
class MosmetroKantsPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    url = 'https://shop.mosmetro.ru/cover_kantselyariya'
    #Locators
    colors_filter = "(//div[@class='t-store__filter__item-title js-store-filter-item-title'])[3]"
    reset_all = '//*[@id="rec414796676"]/div[1]/div/div[1]/div/div[2]/div[1]/div[3]'
    product_variant = "(//span[@class='t-product__option-selected-title'])[1]"
    buy_button = "(//a[@class='js-store-prod-btn2 t-store__card__btn t-store__card__btn_second t-btn t-btn_sm'])[2]"
    new_color_to_buy = '//*[@id="rec414796676"]/div[1]/div/div[3]/div[2]/div[1]/div/form/label[2]'
    cart = "(//div[@class='tn-atom cartcopy'])[1]"
        #Getters
    def get_color_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.colors_filter)))
    def choose_color_fl(self, color):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, f"//span[contains(text(), '{color}')]")))
    def delete_all_filters(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.reset_all)))
    def delete_one_color(self,color):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, f"//div[@data-field-val='{color}']")))
    def get_cover_color(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product_variant)))
    def button_buy(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.buy_button)))

    def go_to_item(self,element):
        actions = ActionChains(self.driver)
        return actions.move_to_element(element).perform()

    def change_color_to_buy(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.new_color_to_buy)))

    def cart_btn(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cart)))



    #Actions
    def change_color(self):
        choosed_colors = 0
        print('Кликнули по кнопке Каталога')
        self.get_color_filter().click()
        print('Выбрали фильтр "Цвет"')
        colors = int(input('Сколько цветов будем выбирать?\n'))
        if colors == 1:
            color = input('Введите цвет (Голубой, желтый, зеленый, Красный, Синий):\n')
            self.choose_color_fl(color).click()
            print('Фильтр применен')
            choosed_colors+=1
        elif colors > 1:
            while choosed_colors < colors:
                color = input('Введите цвет (Голубой, желтый, зеленый, Красный, Синий): ')
                self.choose_color_fl(color).click()
                print('Фильтр применен')
                choosed_colors += 1
                self.get_color_filter().click()
        def delete_filters():
            if choosed_colors > 1:
                self.delete_all_filters().click()
                print('Отбор по цветам удален')
            else:
                self.delete_one_color(color).click()
                print(f'Фильтр цвет "{color}" удален')
        time.sleep(3)
        delete_filters()

    def change_color_without_del(self):
        choosed_colors = 0
        print('Кликнули по кнопке Каталога')
        colors = int(input('Сколько цветов будем выбирать?'))
        if colors == 1:
            self.get_color_filter().click()
            color = input('Введите цвет (Голубой, желтый, зеленый, Красный, Синий): ')
            print('Выбрали фильтр')
            self.choose_color_fl(color).click()
            print('Фильтр применен')
            choosed_colors += 1
        elif colors > 1:
            while choosed_colors < colors:
                self.get_color_filter().click()
                color = input('Введите цвет (Голубой, желтый, зеленый, Красный, Синий): ')
                self.choose_color_fl(color).click()
                print('Фильтр применен')
                time.sleep(2)
                choosed_colors += 1

    def add_to_cart(self):
        self.go_to_item(self.button_buy())
        self.get_cover_color().click()
        time.sleep(1)
        self.change_color_to_buy().click()
        time.sleep(1)
        self.button_buy().click()
        time.sleep(3)
        print('Товар добавлен, ожидаю открытия корзины...')
        self.driver.refresh()
        self.cart_btn().click()
        print('Корзина открыта!')
        time.sleep(2)