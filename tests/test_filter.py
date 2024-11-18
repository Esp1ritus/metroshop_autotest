from selenium import webdriver

from pages.kantselyaria import MosmetroKantsPage
from pages.main_page import MosmetroMainPage


def test_filter(set_up):
    driver = set_up
    metro = MosmetroMainPage(driver)
    metro.getItems()
    metro = MosmetroKantsPage(driver)
    metro.change_color_without_del()