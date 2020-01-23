from pages.product_page import ProductPage
from pages.locators import ProductPageLocators

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
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
])
def test_guest_can_go_to_login_page(browser,link):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser,link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    #time.sleep(180)
    checked_name = page.return_name_of_goods()
    checked_price = page.return_price_of_goods()
    page.check_if_item_added_to_basket(checked_name, checked_price)

@pytest.mark.parametrize('link', [
                                pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207", marks=pytest.mark.xfail),
])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser,link):
    page = ProductPage(browser,link)
    page.open()
    page.add_to_basket()
    assert page.is_not_element_present(*ProductPageLocators.BY_ALERTINNER1), "Object is presented in the page"

@pytest.mark.parametrize('link', [
                                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207",
])
def test_guest_cant_see_success_message(browser,link):
    page = ProductPage(browser,link)
    page.open()
    assert page.is_not_element_present(*ProductPageLocators.BY_ALERTINNER1), "Object is presented in the page"

@pytest.mark.parametrize('link', [
                                pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207", marks=pytest.mark.xfail),
])
def test_message_disappeared_after_adding_product_to_basket(browser,link):
    page = ProductPage(browser,link)
    page.open()
    page.add_to_basket()
    assert page.is_disappeared(*ProductPageLocators.BY_ALERTINNER1), "Object is not disappeared"

