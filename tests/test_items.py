from pages.kantselyaria import MosmetroKantsPage
from pages.main_page import MosmetroMainPage


def test_buy_product(set_up):
    driver = set_up
    metro = MosmetroMainPage(driver)
    metro.getItems()
    kant = MosmetroKantsPage(driver)
    kant.add_to_cart()