from PageObjects.HomePages import HomePage
from Credentials.LoginCred import CredentialsLogin
from TestCases.test_login_page import Test_login_001
from PageObjects.LoginPage import Login
from Locators.LoginLoc import LoginPageLocators



class Test_HomePage_003(Login ):

    def home_page_login(self):
        self.login = Login(self. driver)
        self.login.login_page(LoginPageLocators.text_enter_username, LoginPageLocators.text_eneter_password)
    def home_main_page(self):
        self.verify = HomePage(self.driver)
        self.verify.click_create_acc()



























