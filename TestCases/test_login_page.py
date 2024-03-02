
import time
from selenium import webdriver
from PageObjects.LoginPage import Login
from Credentials.LoginCred import CredentialsLogin
import pytest
from selenium.webdriver.support.wait import WebDriverWait

class Test_login_001(CredentialsLogin):


    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.base_URL)
        self.driver.maximize_window()
        self.login = Login(self.driver)
        self.login.login_page(self.username, self.password)
        time.sleep(10)
        self.chn = self.login.click_login_home()



















