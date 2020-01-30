from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url, "Login link is not found"

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM
        ), "There are not visible login form on the page"

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_FORM
        ), "There are not visible login form on the page"

    def register_new_user(self, email, password):
        email = str(time.time()) + "@fakemailtest.ru"
        password = "AsdFgh123$"
        user_email = self.browser.find_element(
            *LoginPageLocators.EMAIL_ADDRESS)
        user_email.send_keys(email)
        user_password = self.browser.find_element(*LoginPageLocators.PASSWORD1)
        user_password.send_keys(password)
        user_password_verify = self.browser.find_element(
            *LoginPageLocators.PASSWORD2)
        user_password_verify.send_keys(password)
        button_register = self.browser.find_element(
            *LoginPageLocators.BUTTON_REG)
        button_register.click()
        time.sleep(3)
