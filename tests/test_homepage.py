import pytest

from PageObjects.HomePage import HomePage
from TestData.HomePageData import HomePageData
from utilities.baseclass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getdata):
        log = self.getlogger()
        homepage = HomePage(self.driver)

        homepage.getName().send_keys(getdata["Name"])
        homepage.getEmail().send_keys(getdata["Email"])
        homepage.getPassword().send_keys(getdata["Password"])
        homepage.getCheckbox().click()
        self.selectopt(homepage.getGender(), getdata["Gender"])
        log.info("clicking on submit button")
        homepage.submitBtn().click()
        log.info(homepage.allertmesg().text)

        self.driver.refresh()


    @pytest.fixture(params=HomePageData.TestDataforHomePage)
    def getdata(self, request):
        return request.param
