
import time
from selenium import webdriver
from PageObjects.LoginPage import Login
from Credentials.LoginCred import CredentialsLogin
from selenium.webdriver.support.wait import WebDriverWait

class Test_login_001(CredentialsLogin):



    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.base_URL)
        self.lb = Login(self.driver)

        # self.lb.login_button()
        self.lb.enter_user_name(self.username)
        self.driver.implicitly_wait(3)

        self.lb.enter_password(self.password)
        self.driver.implicitly_wait(3)
        self.lb.click_login()




