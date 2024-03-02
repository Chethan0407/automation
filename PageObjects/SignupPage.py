from selenium.webdriver.common.by import By
import time
from Locators.SignupLoc import SignUpLocators
from Credentials.SignupCred import CredentialsSignUp

import random as rd
class SignUp(SignUpLocators, CredentialsSignUp):


    def __init__(self, driver):
        self.driver = driver



    def click_register_tab(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, self.text_signup_button_tagname).click()

    def add_first_name(self, firstname):
        self.driver.find_element(By.ID, self.text_first_name_id).send_keys(firstname)

    def add_last_name(self, lastname):
        self.driver.find_element(By.ID, self.text_last_name_id).send_keys(lastname)

    def add_address(self, add):
        self.driver.find_element(By.ID, self.text_address_id).send_keys(add)

    def add_city(self, city):
        self.driver.find_element(By.ID, self.text_city_id).send_keys(city)

    def add_state(self, state):
        self.driver.find_element(By.ID, self.text_state_id).send_keys(state)

    def add_zip(self, zipcode):
        self.driver.find_element(By.ID, self.text_zip_id).send_keys(zipcode)


    def phone_number(self, phonenumber):
        self.driver.find_element(By.ID, self.text_phonenumber_id).send_keys(phonenumber)

    def ssn(self, ssn):
        self.driver.find_element(By.ID, self.text_ssn_id).send_keys(ssn)

    def username(self, username):
        self.driver.find_element(By.ID, self.text_username_id).send_keys(username)


    def password(self, password):
        self.driver.find_element(By.ID, self.text_password_id).send_keys(password)

    def reconfirm_password(self, rePassword):
        self.driver.find_element(By.ID, self.text_password_confirm_id).send_keys(rePassword)

    def click_register(self):
        self.driver.find_element(By.XPATH, self.text_register_button_xpath).click()





