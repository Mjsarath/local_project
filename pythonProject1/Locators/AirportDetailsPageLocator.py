from selenium.webdriver.common.by import By


class AirportDetailsPageLocator:
    ESTIMATED_TIMES = (By.XPATH, "//tr/td/div/span[contains(text(),'{Delhi}')]/parent::div/ancestor::tr//td["
                                 "@class='ng-binding'][2]'")
    COOKIES_ACCEPT_BUTTON = (By.ID, 'onetrust-accept-btn-handler')
