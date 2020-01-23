from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

class ProductPage(BasePage):
    def add_to_basket(self):
        login_link = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        login_link.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            time.sleep(5)
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def return_name_of_goods(self):
        print(self.browser.find_element(*ProductPageLocators.GOODS_NAME).text)
        return self.browser.find_element(*ProductPageLocators.GOODS_NAME).text
        
    def return_price_of_goods(self):
        print(self.browser.find_element(*ProductPageLocators.GOODS_PRICE).text)
        return self.browser.find_element(*ProductPageLocators.GOODS_PRICE).text

    def check_if_item_added_to_basket(self, goodsname, price):
        alertinner1 = self.browser.find_element(*ProductPageLocators.BY_ALERTINNER1)
        print(alertinner1.text)
        assert goodsname in alertinner1.text, "The item has not been added to basket"
        alertinner2 = self.browser.find_element(*ProductPageLocators.BY_ALERTINNER2)
        print(alertinner2.text)
        assert "Your basket now qualifies" in alertinner2.text, "Your basket now are not qualified for the Deferred benefit offer"
        alertinner3 = self.browser.find_element(*ProductPageLocators.BY_ALERTINNER3)
        print(alertinner3.text)
        assert price in alertinner3.text, "Total basket sum is not presented"

