from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators(object):
    REG_FORM = (By.CSS_SELECTOR, "#id_registration-email")
    LOGIN_FORM = (By.CSS_SELECTOR, "#id_login-username")