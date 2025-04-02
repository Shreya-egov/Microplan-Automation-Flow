import pytest
import time
import os
import allure
from pageobjects.Microplan import TestMPFlow
from utilities.readProperties import ReadConfig
from utilities.customlogger import LogGen


@allure.suite('Test Microplan Flow')  # Suite for this test
@allure.feature('Microplan Test Flow')  # General feature for the whole flow
class TestMPLoginFlow:
    baseURL = ReadConfig.get_application_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    country_name = ReadConfig.get_country_name()
    logger = LogGen.loggen()

    @pytest.fixture(autouse=True)
    def setup(self, setup):
        self.driver = setup  # WebDriver setup
        
        # Ensure that the driver quits after the test, regardless of pass/failure
        yield self.driver
        
        # Cleanup / Teardown: Quit the driver after the test
        self.driver.quit()   # Ensures the driver quits regardless of any test failure

    @allure.story('Step 1: Perform Login')
    def test_complete_flow(self):
        # Step 1: Perform Login
        self.logger.info(f"***************Opening URL: {self.baseURL}*****************")
        allure.dynamic.feature('Login')  # Dynamic feature tag for the login step
        self.logger.info("*****************Performing login actions*******************")
        self.driver.get(self.baseURL)
        lp = TestMPFlow(self.driver)
        
        lp.setusername(self.username)
        lp.setpassword(self.password)
        lp.setcountry(self.country_name)
        lp.dpp()
        lp.login()
        self.logger.info("***********Logging successful***************")

        # Ensure successful login
        act_title = self.driver.title
        assert act_title == "DIGIT HCM", f"Expected title 'DIGIT HCM' but got '{act_title}'"
        
        # Step 2: Navigate to Microplan creation
        allure.dynamic.feature('Microplan Setup')  # Dynamic feature tag for microplan setup
        lp.get_setup_microplan_element()
        lp.nextbuttonone()
        lp.set_unique_microplan_name()
        self.logger.info("**********Microplan name initiated*****************")
        lp.nextbuttonone()
        lp.popprocceed()
        lp.countrydropdown()
        # lp.countrydropdown(self.countrydrop)

        # Step 3: Select Boundaries for the Microplan
        allure.dynamic.feature('Boundary Selection')  # Dynamic feature tag for boundary selection
        self.logger.info("***************Selecting boundaries*****************")
        lp.provincedropdown()
        lp.BG1click()
        lp.districtdropdown()
        lp.BG1click()
        lp.APdropdown()
        lp.BG1click()
        lp.Localitydropdown()
        lp.BG1click()
        lp.VillageDropdown()
        lp.BG1click()
        lp.nextbuttonone()
        self.logger.info("*******Boundaries for Microplan are selected********")

        # Step 4: Upload Population and Facility Details
        allure.dynamic.feature('Data Upload')  # Dynamic feature tag for data upload
        lp.upload_Pop_excel_file()
        lp.nextbuttonone()
        self.logger.info("********Population excel uploaded successfully*******")
        lp.upload_Facility_excel_file()
        lp.nextbuttonone()
        self.logger.info("**********Facilities excel uploaded successfully***********")
        lp.selectTogetherProcess()
        lp.nextbuttonone()

        # Step 5: Add Assumptions and Estimations
        allure.dynamic.feature('Assumptions and Estimations')  # Dynamic feature tag for assumptions
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
        self.logger.info("*********Assumptions and estimations are successfully loaded********")

        # Step 6: Tag Users for the Microplan
        allure.dynamic.feature('User Tagging')  # Dynamic feature tag for user tagging
        lp.tagNMP()
        lp.nextbuttontwo()
        lp.tagNFA()
        lp.nextbuttontwo()
        lp.tagNPA()
        lp.nextbuttontwo()
        self.logger.info("***********Users tagged successfully*********")
        lp.nextbuttontwo()
        lp.nextbuttontwo()
        lp.nextbuttonone()
        lp.nextbuttonone()


        # Step 7: Create the Microplan
        allure.dynamic.feature('Microplan Creation')  # Dynamic feature tag for microplan creation
        lp.createMicroplan()
        self.logger.info("******Microplan created successfully******")

        # Optionally: Take screenshot after creating the microplan
        # screenshot_folder = "./Screenshots"
        # if not os.path.exists(screenshot_folder):
        #     os.makedirs(screenshot_folder)

        # timestamp = time.strftime("%Y%m%d-%H%M%S")
        # screenshot_filename = os.path.join(screenshot_folder, f"createMP_{timestamp}.png")
        # self.driver.save_screenshot(screenshot_filename)
        # logging.info(f"Screenshot saved at {screenshot_filename}")
        
        # logging.info("Microplan created successfully")
