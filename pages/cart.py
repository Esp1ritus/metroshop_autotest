import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import *


# наследуем класс Base
class MosmetroCart(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    item_count_plus = "//span[@class='t706__product-plus']"
    name = "//input[@id='input_1496239431201']"
    email = "//input[@id='input_1496239459190']"
    phone = "//input[@id='input_1496239478607']"
    delivery_time = "(//div[@class='t-radio__indicator'])[2]"
    street_field = '//*[@id="street-searchbox"]/div[1]/div[1]/div[2]/input'
    street_choice = '//*[@id="street-searchbox"]/div[1]/div[2]/div/div[3]'
    house = "(//input[@class='js-tilda-rule t-input'])[1]"
    podiezd = "(//input[@class='js-tilda-rule t-input'])[2]"
    floor = "(//input[@class='js-tilda-rule t-input'])[3]"
    flat = "(//input[@class='js-tilda-rule t-input'])[4]"
    doorpass = "(//input[@class='js-tilda-rule t-input'])[5]"
    accept_data = '//*[@id="form178869761"]/div[2]/div[6]/div/label/div'
    confirm = '//*[@id="form178869761"]/div[2]/div[10]/button'
    success_text = 'Спасибо за покупку! Менеджер свяжется с вами для подтверждения заказа!'
    text_locator = "//div[@class='js-successbox t-form__successbox t-text t-text_md']"
    payment_type = "(//div[@class='t-radio__indicator'])[6]"

    # Getters
    def get_color_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.item_count_plus)))

    def plus_one_item(self):
        self.get_color_filter().click()

    def name_field(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.name)))

    def email_field(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.email)))

    def phone_field(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.phone)))

    def delivery_time_radiobtn(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.delivery_time)))

    def dev_street_field(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.street_field)))

    def dev_street_choice(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.street_choice)))

    def home_val(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.house)))

    def podjezd_val(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.podiezd)))

    def floor_val(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.floor)))

    def flat_val(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.flat)))

    def doorpass_val(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.doorpass)))

    def accept_checkbox(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.accept_data)))

    def confirm_btn(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.confirm)))

    def final_text(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.text_locator)))

    def change_payment_type(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.payment_type)))

    def buy_element(self):
        self.plus_one_item()
        print('Увеличили количество товаров (+1)')
        self.name_field().send_keys('Sergey')
        self.email_field().send_keys('example@ya.ru')
        self.phone_field().send_keys('9005003300')
        print('Заполнены поля для имени, почты, телефона')
        self.delivery_time_radiobtn().click()
        print('Выбрали время доставки')
        self.dev_street_field().click()
        self.dev_street_choice().click()
        self.home_val().send_keys('15')
        self.podjezd_val().send_keys('2')
        self.floor_val().send_keys('15')
        self.flat_val().send_keys('38')
        self.doorpass_val().send_keys('121345')
        self.accept_checkbox().click()
        self.change_payment_type().click()
        self.confirm_btn().click()
        time.sleep(3)
        text = self.final_text().text
        print(text)
        assert text == self.success_text, 'Текст не совпадает! Что-то не так!'
        print('Заказ успешно оформлен!')