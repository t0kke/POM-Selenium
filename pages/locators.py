from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators(object):
    REG_FORM = (By.CSS_SELECTOR, "id_registration-email")
    LOGIN_FORM = (By.CSS_SELECTOR, "id_login-username")


class ProductPageLocators(object):
    ADD_TO_CART = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    TITLE_BOOK  = (By.CSS_SELECTOR, "div.product_main > h1")
    PRICE_BOOK = (By.CSS_SELECTOR, "div.product_main > p.price_color")
    ALERT_TITLE_BOOK = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    ALERT_PRICE_BOOK = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')

