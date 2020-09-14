from .locators import LoginPageLocators
from .base_page import BasePage
from selenium.webdriver.common.by import By
from .login_page import LoginPage
from .locators import MainPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        alert = self.browser.switch_to.alert
        alert.accept()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_registration_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not found"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not found"



