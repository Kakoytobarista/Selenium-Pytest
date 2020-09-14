from selenium.common.exceptions import NoAlertPresentException
from pages.product_page import ProductPage
import time
import pytest


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.check_name_product_in_string_basket()
    time.sleep(5)
    page.check_price_product_in_price_basket()
    time.sleep(3)
