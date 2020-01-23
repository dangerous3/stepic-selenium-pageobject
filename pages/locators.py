from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class LoginPageLocators():
    REGISTRATION_FORM = (By.ID, "id_registration-email")
    LOGIN_FORM = (By.ID, "id_login-username")

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR,".btn-add-to-basket")
    BY_ALERTINNER1 = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    BY_ALERTINNER3 = (By.XPATH, '//*[@id="messages"]/div[3]/div/p/strong')
    GOODS_NAME = (By.CSS_SELECTOR, 'div.product_main h1')
    GOODS_PRICE = (By.CSS_SELECTOR, 'p.price_color')
