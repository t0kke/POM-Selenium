from .cart_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in str(self.browser.current_url), "Link does not contain login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Registration form is not presented"

    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        email_input = self.browser.find_element(*LoginPageLocators.REG_FORM)
        email_input.send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWRD).send_keys("wSkMq$AaG!wd76L")
        self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWRD).send_keys("wSkMq$AaG!wd76L")
        self.browser.find_element(*LoginPageLocators.BTN_REGISTER).click()





