import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.CheckoutPage import CheckOutPage
from PageObjects.ConfirmPage import ConfirmPage
from PageObjects.HomePage import HomePage
from utilities.baseclass import BaseClass


class Teste2e(BaseClass):
    def test_e2e(self):
        log = self.getlogger()
        homepage = HomePage(self.driver)

        checkoutpage = homepage.shopele()

        cards = checkoutpage.getCardtitles()
        i = -1
        for card in cards:
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkoutpage.getCardfooter()[i].click()

        checkoutpage.getcheckoutItems().click()

        confirmpage = checkoutpage.getAnothercheckout()
        log.info("entering Ind")
        confirmpage.putCountry().send_keys("ind")
        self.verifyTxtPresence("India")
        confirmpage.indiaLink().click()

        confirmpage.checkBox().click()
        confirmpage.purachBtn().click()
        txt = confirmpage.alertMsg().text
        log.info(confirmpage.alertMsg().text)
        assert "fail" in txt
