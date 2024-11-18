from pages.main_page import MosmetroMainPage


def test_search(set_up):
    driver = set_up
    metro = MosmetroMainPage(driver)
    metro.find_search('Карта')
