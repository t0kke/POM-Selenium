from pages.product_page import ProductPage
import time


def test_guest_can_add_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    time.sleep(3)
    page.should_be_product_name_match()
    page.should_be_price_product_corresponds_to_price_in_basket()

