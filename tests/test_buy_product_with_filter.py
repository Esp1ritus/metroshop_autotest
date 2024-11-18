from pages.cart import MosmetroCart
from pages.kantselyaria import MosmetroKantsPage
from pages.main_page import MosmetroMainPage


def test_buy_product_with_filter(set_up):
    driver = set_up
    metro = MosmetroMainPage(driver)
    metro.getItems()
    metro = MosmetroKantsPage(driver)
    metro.change_color_without_del()
    metro.add_to_cart()
    cart = MosmetroCart(driver)
    cart.buy_element()