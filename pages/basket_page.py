from .base_page import BasePage
from selenium import webdriver
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def check_if_basket_is_not_contain_items(self):
        assert self.is_not_element_present(
            *BasketPageLocators.PROCEED_TO_CHECKOUT), "Basket is not empty"

    def check_if_basket_has_empty_message(self):
        assert self.is_element_present(
            *BasketPageLocators.BASKET_IS_EMPTY
        ), "Empty basket message is not presented"
