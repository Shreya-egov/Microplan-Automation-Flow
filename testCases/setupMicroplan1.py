import pytest
import time
import os
from pageobjects.LoginpageDEMO import Loginpage
from utilities.readProperties import ReadConfig
from utilities.customlogger import logging


class TestLoginFlow:
    baseURL = ReadConfig.get_application_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    country_name = ReadConfig.get_country_name()
    countrydrop = ReadConfig.get_country()
    provincedrop = ReadConfig.get_province()
    districtdrop = ReadConfig.get_district()
    APdrop = ReadConfig.get_AP()

    @pytest.fixture(autouse=True)
    def setup(self, setup):
        self.driver = setup  # WebDriver setup
        
        # Ensure that the driver quits after the test, regardless of pass/failure
        yield self.driver
        
        # Cleanup / Teardown: Quit the driver after the test
        self.driver.quit()   # Ensures the driver quits regardless of any test failure


    def test_complete_flow(self):
        logging.info(f"Opening URL: {self.baseURL}")
        self.driver.get(self.baseURL)
        lp = Loginpage(self.driver)
        
        # Step 1: Perform Login
        logging.info("Performing login actions")
        lp.setusername(self.username)
        lp.setpassword(self.password)
        lp.setcountry(self.country_name)
        lp.dpp()
        lp.login()

        # Ensure successful login
        act_title = self.driver.title
        assert act_title == "DIGIT HCM", f"Expected title 'DIGIT HCM' but got '{act_title}'"
        logging.info("Login successful, title verified")

        # Step 2: Navigate to Microplan creation
        logging.info("Navigating to the Microplan creation")
        lp.get_setup_microplan_element()
        lp.nextbuttonone()
        lp.set_unique_microplan_name()
        lp.nextbuttonone()
        lp.popprocceed()
        lp.countrydropdown(self.countrydrop)
        
        # Step 3: Select Boundaries for the Microplan
        logging.info("Selecting boundaries for the microplan")
        
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

        # Step 4: Upload Population and Facility Details
        logging.info("Uploading population and facility details")
        lp.upload_Pop_excel_file()
        lp.nextbuttonone()
        lp.upload_Facility_excel_file()
        lp.nextbuttonone()
        lp.selectTogetherProcess()
        lp.nextbuttonone()

        # Step 5: Add Assumptions and Estimations
        logging.info("Adding assumptions and estimations")
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

        # Step 6: Tag Users for the Microplan
        logging.info("Tagging users for the microplan")
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

        # Step 7: Create the Microplan
        logging.info("Creating the microplan")
        lp.createMicroplan()

        # # Optionally: Take screenshot after creating the microplan
        # screenshot_folder = "./Screenshots"
        # if not os.path.exists(screenshot_folder):
        #     os.makedirs(screenshot_folder)

        # timestamp = time.strftime("%Y%m%d-%H%M%S")
        # screenshot_filename = os.path.join(screenshot_folder, f"createMP_{timestamp}.png")
        # self.driver.save_screenshot(screenshot_filename)
        # logging.info(f"Screenshot saved at {screenshot_filename}")

        # logging.info("Microplan created successfully")
