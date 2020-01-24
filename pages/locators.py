from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    REGISTRATION_FORM = (By.ID, "id_registration-email")
    LOGIN_FORM = (By.ID, "id_login-username")
    EMAIL_ADDRESS = (By.CSS_SELECTOR,"#id_registration-email") 
    PASSWORD1 = (By.CSS_SELECTOR,"#id_registration-password1")
    PASSWORD2 = (By.CSS_SELECTOR,"#id_registration-password2")
    BUTTON_REG = (By.XPATH,"//button[@value='Register']")

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR,".btn-add-to-basket")
    BY_ALERTINNER1 = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    BY_ALERTINNER3 = (By.XPATH, '//*[@id="messages"]/div[3]/div/p/strong')
    GOODS_NAME = (By.CSS_SELECTOR, 'div.product_main h1')
    GOODS_PRICE = (By.CSS_SELECTOR, 'p.price_color')
