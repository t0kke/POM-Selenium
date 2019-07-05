from .cart_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_product_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_ITEMS), "The basket is empty"

    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "The basket is not empty"

    def should_be_message_basket_is_empty(self):
        assert "Your basket is empty." in self.browser.find_element(*BasketPageLocators.MESS_BASKET_EMPTY).text, "No message that the basket is empty"

