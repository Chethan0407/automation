import time

from PageObjects.SignupPage import SignUp
from Credentials.SignupCred import CredentialsSignUp
from Credentials.LoginCred import CredentialsLogin
import pytest



class Test_Login_002(CredentialsSignUp, CredentialsLogin):

    #@pytest.mark.sanity
    def test_sign_up(self, setup):
        self.driver = setup
        self.driver.get(self.base_URL)
        self.driver.maximize_window()
        self.sp = SignUp(self.driver)



        #invokin test cases

        self.sp.click_register_tab()
        time.sleep(3)
        self.sp.add_first_name(self.firstname)
        time.sleep(3)
        self.sp.add_last_name(self.lastname)
        time.sleep(3)
        self.sp.add_address(self.add)
        time.sleep(3)
        self.sp.add_city(self.city)
        time.sleep(3)
        self.sp.add_state(self.state)
        time.sleep(3)
        self.sp.add_zip(self.zipcode)
        time.sleep(3)
        self.sp.phone_number(self.phonenumber)
        time.sleep(3)
        self.sp.ssn(self.ssn)
        time.sleep(3)
        self.sp.username(self.username)
        time.sleep(3)
        print("the usernmae is", self.username)
        self.sp.password(self.password)
        time.sleep(3)
        print("the password is", self.password)
        self.sp.reconfirm_password(self.rePassword)
        time.sleep(3)
        self.sp.click_register()

        time.sleep(3)

        title = self.driver.title
        if title == "welcome" + self.username:
            assert True
            print("correct")
        else:
            pass
            print("fail machi")
            time.sleep(10)


























