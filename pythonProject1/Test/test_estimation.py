from concurrent.futures import thread

from Constants.Base_Constant import Base_Constants
from Pages.AirportDetailPage import AirportDetailPage
from Test.test_base import BaseTest
from Locators.AirportDetailsPageLocator import AirportDetailsPageLocator


class TestEstimation(BaseTest):

    def test_estimate(self,request):
        location = Base_Constants.LOCATION_TO_BE_CHECKED
        # AirportDetailsPageLocator.ESTIMATED_TIMES
        self.airport_detail_page = AirportDetailPage(self.driver)
        self.airport_detail_page.click(AirportDetailsPageLocator.COOKIES_ACCEPT_BUTTON)
        print("Hello")
