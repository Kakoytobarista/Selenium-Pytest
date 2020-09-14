from selenium.common.exceptions import NoSuchElementException


class BasePage(object):
    def __init__(self, browser, url, timeout=10):
        """Конструктор класса.
        :param browser:
        :param url:
        """
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        """метод открывает нужную страницу,
        используя метод get()
        """
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def alert_two(self):
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

