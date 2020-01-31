from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.locators import ProductPageLocators
from pages.locators import BasketPageLocators

def test_guest_should_see_login_link(browser):
    link = ProductPageLocators.MAIN_PAGE_URL
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_login_or_register_form_should_be_present(browser):
    link = ProductPageLocators.LOGIN_URL
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()
    page.should_be_login_form()
    page.should_be_register_form()

def test_guest_can_go_to_login_page(browser):
    link = ProductPageLocators.MAIN_PAGE_URL
    page = MainPage(browser, link)
    page.open()
    login_page = page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = ProductPageLocators.MAIN_PAGE_URL
    page = MainPage(browser, link)
    page.open()
    basket_page = page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.check_if_basket_is_not_contain_items()
    basket_page.check_if_basket_has_empty_message()
    

