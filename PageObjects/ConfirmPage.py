from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    country = (By.CSS_SELECTOR, "#country")

    checkbox = (By.XPATH, "//div[@class ='checkbox checkbox-primary']")

    purchaseBtn = (By.XPATH, "//input[@value='Purchase']")

    alertmsg = (By.CLASS_NAME, "alert-success")

    indialink = (By.LINK_TEXT, "India")

    def putCountry(self):
        return self.driver.find_element(*ConfirmPage.country)

    def checkBox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def purachBtn(self):
        return self.driver.find_element(*ConfirmPage.purchaseBtn)

    def alertMsg(self):
        return self.driver.find_element(*ConfirmPage.alertmsg)

    def indiaLink(self):
        return self.driver.find_element(*ConfirmPage.indialink)
