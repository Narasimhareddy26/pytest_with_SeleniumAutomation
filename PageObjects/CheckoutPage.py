from selenium.webdriver.common.by import By

from PageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    cardtitles = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkoutItems = (By.XPATH, "//a[@class='nav-link btn btn-primary']")

    anotherCheckout = (By.XPATH, "//button[@class='btn btn-success']")
    def getCardtitles(self):
        return self.driver.find_elements(*CheckOutPage.cardtitles)

    def getCardfooter(self):
        return  self.driver.find_elements(*CheckOutPage.cardFooter)
    def getcheckoutItems(self):
        return self.driver.find_element(*CheckOutPage.checkoutItems)

    def getAnothercheckout(self):
        self.driver.find_element(*CheckOutPage.anotherCheckout).click()
        confirmpage = ConfirmPage(self.driver)
        return confirmpage