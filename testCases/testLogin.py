import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from testCases.confTest import startUp
from utilities.readProperties import ReadConfig
from utilities.Logger import LogGen


class Test_001_Login:
    baseUrl = ReadConfig.getAppURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.log_generator()

    def test_homePageTitle(self, startUp):
        self.logger.info("**************Test 001 Login****************")
        self.logger.info("**************Verifying Home Page Title**********")
        self.driver = startUp
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Your store. Login":
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("**************Fail test Home Page Title**************")
            assert False

    def test_login(self, startUp):
        self.logger.info("*****************Verifying Login Test*************")
        self.driver = startUp
        self.driver.get(self.baseUrl)
        # Create LoginPage obj
        self.loginPage = LoginPage(self.driver)
        # Set Credentials
        self.loginPage.setUserName(self.username)
        self.loginPage.setPassword(self.password)
        self.loginPage.clickLogin()
        # Verify Title
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info("******************Login Success**********************")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_login.png")
            self.driver.close()
            self.logger.error("*****************Failed Login**************")
            assert False
