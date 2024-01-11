from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.web_driver_timeout = 10

    def click(self, element):
        """To click the desired web element (Waits till the element is visible)
        :param : element - Web element that needs to be clicked"""
        WebDriverWait(self.driver, self.web_driver_timeout).until(EC.element_to_be_clickable(element)).click()

    def get_page_title(self):
        """To return the title of the current page
        :returns: Title of the page"""
        return self.driver.title

    def get_page_url(self):
        """To return the updated url
        :returns: returns the URL of the page"""
        return self.driver.current_url

    def wait_for_page_url(self, page_url):
        """Waits for the page to be loaded
        :param:page_url - URL that needs to be waited for or loaded
        :returns: True-when the URL is loaded
        """
        WebDriverWait(self.driver, self.web_driver_timeout).until(EC.url_contains(page_url))
        return True

    def navigate_to_url(self, page_url):
        """To change the URL to the desired page
        :param: page_url - URL that needs to be changed"""
        self.driver.get(page_url)

    def get_text(self, element):
        locator = WebDriverWait(self.driver, self.web_driver_timeout).until(EC.presence_of_element_located(element))
        return locator.text.strip()
