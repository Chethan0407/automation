from selenium.webdriver.common.by import By
import time
from Locators.HomepageLoc import Homepagelocators
from PageObjects.Basepage import BasePage


class HomePage(BasePage, Homepagelocators,):

    def click_create_acc(self):
        super().__init__(self.driver)
        self.driver.find_element(By.PARTIAL_LINK_TEXT, self.text_open_new_account_pl)



