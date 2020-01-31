from pages.product_page import ProductPage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait

import time
import pytest


@pytest.mark.parametrize('link', [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    pytest.param(
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
        marks=pytest.mark.xfail),
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
])
def test_guest_can_go_to_login_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    checked_name = page.return_name_of_goods()
    checked_price = page.return_price_of_goods()
    page.check_if_item_added_to_basket(checked_name, checked_price)


@pytest.mark.user_login
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = ProductPageLocators.LOGIN_URL
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemailtest.ru"
        password = "AsdFgh123$"
        page.register_new_user(email, password)
        page.should_be_authorized_user()
        time.sleep(5)

    def test_user_can_add_product_to_basket(self, browser):
        link = ProductPageLocators.SHELLCODERS_HANDBOOK_URL
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        checked_name = page.return_name_of_goods()
        checked_price = page.return_price_of_goods()
        page.check_if_item_added_to_basket(checked_name, checked_price)

    def test_user_cant_see_success_message(self, browser):
        link = ProductPageLocators.CODERS_AT_WORK_URL
        page = ProductPage(browser, link)
        page.open()
        page.check_not_visible_success_message()


def test_guest_can_go_to_login_page(browser):
    link = ProductPageLocators.MAIN_PAGE_URL
    page = MainPage(browser, link)
    page.open()
    login_page = page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_can_add_product_to_basket(browser):
    link = ProductPageLocators.SHELLCODERS_HANDBOOK_URL
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    checked_name = page.return_name_of_goods()
    checked_price = page.return_price_of_goods()
    page.check_if_item_added_to_basket(checked_name, checked_price)


@pytest.mark.parametrize('link', [
    pytest.param(ProductPageLocators.CODERS_AT_WORK_URL,
                 marks=pytest.mark.xfail),
])
def test_guest_cant_see_success_message_after_adding_product_to_basket(
    browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.check_not_visible_success_message()


@pytest.mark.parametrize('link', [ProductPageLocators.CODERS_AT_WORK_URL])
def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.check_not_visible_success_message()


@pytest.mark.parametrize('link', [
    pytest.param(ProductPageLocators.CODERS_AT_WORK_URL,
                 marks=pytest.mark.xfail),
])
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.check_not_visible_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = ProductPageLocators.THE_CITY_AND_THE_STARS_URL
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = ProductPageLocators.THE_CITY_AND_THE_STARS_URL
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = ProductPageLocators.CODERS_AT_WORK_URL
    page = ProductPage(browser, link)
    page.open()
    basket_page = page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.check_if_basket_is_not_contain_items()
    basket_page.check_if_basket_has_empty_message()
