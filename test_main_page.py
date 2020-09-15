from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages. base_page import BasePage
from pages.basket_page import BasketPage
import pytest


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


def test_guest_should_see_login_link(self, browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = MainPage(page.browser, page.browser.current_url)
    login_page.should_be_login_link()


# def test_guest_should_see_registration_form(browser):
#     link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
#     page = MainPage(browser, link)
#     page.open()
#     page.should_be_registration_form()
#
#
# def test_guest_should_see_login_form(browser):
#     link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
#     page = MainPage(browser, link)
#     page.open()
#     page.should_be_login_form()
