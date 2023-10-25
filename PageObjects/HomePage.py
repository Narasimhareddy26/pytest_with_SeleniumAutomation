from selenium.webdriver.common.by import By

from PageObjects.CheckoutPage import CheckOutPage


class HomePage:
    shop = (By.LINK_TEXT, "Shop")
    email = (By.CSS_SELECTOR, "input[name='email']")
    name = (By.NAME, "name")
    checkbox = (By.ID, "exampleCheck1")
    submit = (By.XPATH, "//input[@type='submit']")
    alrtMsg = (By.CLASS_NAME, "alert-success")
    password = (By.CSS_SELECTOR, "input[id=exampleInputPassword1]")
    gender = (By.ID, "exampleFormControlSelect1")

    def __init__(self, driver):
        self.driver = driver

    def shopele(self):
        self.driver.find_element(*HomePage.shop).click()  # "*" means going as tuple
        checkoutpage = CheckOutPage(self.driver)
        return checkoutpage

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getCheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def submitBtn(self):
        return self.driver.find_element(*HomePage.submit)

    def allertmesg(self):
        return self.driver.find_element(*HomePage.alrtMsg)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)