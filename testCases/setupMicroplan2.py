import pytest
import time
import os
import allure
from pageobjects.LoginpageDEMO import Loginpage
from utilities.readProperties import ReadConfig
from utilities.customlogger import LogGen


class TestMPFlow:
    baseURL = ReadConfig.get_application_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    country_name = ReadConfig.get_country_name()
    countrydrop = ReadConfig.get_country()
    provincedrop = ReadConfig.get_province()
    districtdrop = ReadConfig.get_district()
    APdrop = ReadConfig.get_AP()

    logger = LogGen.loggen()

    @pytest.fixture(autouse=True)
    def setup(self, setup):
        self.driver = setup  # WebDriver setup
        
        # Ensure that the driver quits after the test, regardless of pass/failure
        yield self.driver
        
        # Cleanup / Teardown: Quit the driver after the test
        self.driver.quit()   # Ensures the driver quits regardless of any test failure


    @allure.feature("Login Feature")
    @allure.story("User login with valid credentials")
    @allure.title("Test Login Functionality")
    @allure.description("This test case tests the login functionality of the application")
    def test_login(self):
        self.logger.info(f"Opening URL: {self.baseURL}")
        self.driver.get(self.baseURL)
        lp = Loginpage(self.driver)

        # Step 1: Perform Login
        self.logger.info("Performing login actions")
        lp.setusername(self.username)
        lp.setpassword(self.password)
        lp.setcountry(self.country_name)
        lp.dpp()
        lp.login()

        # Ensure successful login
        act_title = self.driver.title
        assert act_title == "DIGIT HCM", f"Expected title 'DIGIT HCM' but got '{act_title}'"
        self.logger.info("Login successful, title verified")


    @allure.feature("Microplan Feature")
    @allure.story("Microplan Creation and Setup")
    @allure.title("Test Microplan Creation")
    @allure.description("This test case ensures the microplan creation is successful")
    def test_microplan_creation(self):
        self.logger.info("Navigating to the Microplan creation")
        lp = Loginpage(self.driver)

        lp.get_setup_microplan_element()
        lp.nextbuttonone()
        lp.set_unique_microplan_name()
        lp.nextbuttonone()
        lp.popprocceed()
        lp.countrydropdown(self.countrydrop)

        # Step 2: Select Boundaries for the Microplan
        self.logger.info("Selecting boundaries for the microplan")
        lp.provincedropdown(self.provincedrop)
        lp.BG1click()
        lp.districtdropdown(self.districtdrop)
        lp.BG1click()
        lp.APdropdown(self.APdrop)
        lp.BG1click()
        lp.Localitydropdown()
        lp.BG1click()
        lp.VillageDropdown()
        lp.BG1click()
        lp.nextbuttonone()

    
    @allure.feature("File Upload Feature")
    @allure.story("Population and Facility File Upload")
    @allure.title("Test Population and Facility Upload")
    @allure.description("This test case uploads population and facility files for the microplan")
    def test_population_facility_upload(self):
        self.logger.info("Uploading population and facility details")
        lp = Loginpage(self.driver)

        lp.upload_Pop_excel_file()
        lp.nextbuttonone()
        lp.upload_Facility_excel_file()
        lp.nextbuttonone()
        lp.selectTogetherProcess()
        lp.nextbuttonone()

 
    @allure.feature("Assumptions Feature")
    @allure.story("Adding Assumptions and Estimations")
    @allure.title("Test Assumptions and Estimations")
    @allure.description("This test case adds assumptions and estimations for the microplan")
    def test_assumptions_estimations(self):
        self.logger.info("Adding assumptions and estimations")
        lp = Loginpage(self.driver)

        lp.Genassumptions()
        lp.nextbuttontwo()
        lp.HRassump()
        lp.nextbuttontwo()
        lp.commodassump()
        lp.nextbuttontwo()
        lp.nextbuttonone()
        lp.nextbuttontwo()
        lp.nextbuttontwo()
        lp.nextbuttontwo()
        lp.nextbuttonone()

    @allure.feature("User Tagging Feature")
    @allure.story("Tagging Users for the Microplan")
    @allure.title("Test User Tagging")
    @allure.description("This test case tags users to the microplan")
    def test_tagging_users(self):
        self.logger.info("Tagging users for the microplan")
        lp = Loginpage(self.driver)

        lp.tagNMP()
        lp.nextbuttontwo()
        lp.tagNFA()
        lp.nextbuttontwo()
        lp.tagNPA()
        lp.nextbuttontwo()
        lp.nextbuttontwo()
        lp.nextbuttontwo()
        lp.nextbuttonone()
        lp.nextbuttonone()


    @allure.feature("Microplan Creation Feature")
    @allure.story("Microplan Finalization")
    @allure.title("Test Microplan Creation")
    @allure.description("This test case creates the final microplan")
    def test_create_microplan(self):
        self.logger.info("Creating the microplan")
        lp = Loginpage(self.driver)

        lp.createMicroplan()
