from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTRATION_FORM = (By.ID, "id_registration-email")
    LOGIN_FORM = (By.ID, "id_login-username")
