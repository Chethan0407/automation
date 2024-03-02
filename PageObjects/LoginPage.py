import pytest
from selenium.webdriver.common.by import By
import time
from Locators.LoginLoc import LoginPageLocators
from PageObjects.Basepage import BasePage



class Login(BasePage):




    # action methods
    def login_page(self, username, password):
        super().__init__(self.driver)
        self.driver.find_element(By.NAME, LoginPageLocators.text_enter_username).send_keys(username)
        self.driver.find_element(By.NAME, LoginPageLocators.text_eneter_password).send_keys(password)

    def click_login_home(self):
        self.driver.find_element(By.XPATH, LoginPageLocators.text_click_login).click()














