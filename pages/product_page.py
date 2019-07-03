from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_cart(self):
        btn_add_to_cart = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        btn_add_to_cart.click()

    def should_be_button_add_product(self):
        assert self.browser.find_element(*ProductPageLocators.ADD_TO_CART), "Button add to cart is not presented"

    def should_be_product_name_match(self):
        assert self.browser.find_element(*ProductPageLocators.TITLE_BOOK).text == self.browser.find_element(*ProductPageLocators.ALERT_TITLE_BOOK).text, \
            "Book title {} does not match {}".format(self.browser.find_element(*ProductPageLocators.TITLE_BOOK).text, self.browser.find_element(*ProductPageLocators.ALERT_TITLE_BOOK).text)

    def should_be_price_product_corresponds_to_price_in_basket(self):
        assert self.browser.find_element(*ProductPageLocators.PRICE_BOOK).text == self.browser.find_element(*ProductPageLocators.ALERT_PRICE_BOOK).text, "Product price does not match the price in the basket"

