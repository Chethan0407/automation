
from selenium.webdriver.common.by import By
import time
from Locators.LoginLoc import LoginPageLocators

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC










class Login(LoginPageLocators):
    def __init__(self, driver):
        self.driver = driver
        time.sleep(10)

    # action methods
    def enter_user_name(self, mobilenumber):
        self.driver.find_element(By.NAME, self.text_enter_username).send_keys(mobilenumber)


    def enter_password(self, password):
        self.driver.find_element(By.NAME, self.text_eneter_password).send_keys(password)



    def click_login(self):
        self.driver.find_element(By.XPATH, self.text_click_login).click()










