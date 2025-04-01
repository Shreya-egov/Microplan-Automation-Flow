import pytest
from pageobjects.LoginpageDEMO import Loginpage
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.readProperties import ReadConfig

class TestLogin:
    baseURL = ReadConfig.get_application_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    country_name = ReadConfig.get_country_name()
    Bednet_name = ReadConfig.get_bednet_name()
    countrydrop = ReadConfig.get_country()
    provincedrop = ReadConfig.get_province()
    districtdrop = ReadConfig.get_district()
    APdrop = ReadConfig.get_AP()
    

    def test_login(self, setup):
        driver = setup
        driver.get(self.baseURL)
        lp = Loginpage(driver)
        
        lp.setusername(self.username)
        lp.setpassword(self.password)
        lp.setcountry(self.country_name)
        
        lp.dpp()
        lp.login()
        
        # Ensure successful login
        act_title = driver.title
        assert act_title == "DIGIT HCM", f"Expected title 'DIGIT HCM' but got '{act_title}'"
        
        # Navigate and perform actions on the next page
        lp.get_setup_microplan_element()
        lp.nextbuttonone()
        lp.set_unique_microplan_name()
        lp.nextbuttonone()
        lp.popprocceed()
        lp.countrydropdown(self.countrydrop)
        # lp.countrydropdown
        lp.provincedropdown(self.provincedrop)
        # lp.provincedropdown
        lp.BG1click()
        # lp.BG2click()
        lp.districtdropdown(self.districtdrop)
        # lp.districtdropdown
        lp.BG1click()
        # lp.BG1click()
        lp.APdropdown(self.APdrop)
        # lp.APdropdown
        lp.BG1click()
        lp.Localitydropdown()
        lp.BG1click()
        lp.VillageDropdown()
        lp.BG1click()
        lp.nextbuttonone()
        lp.upload_Pop_excel_file()
        lp.nextbuttonone()
        lp.upload_Facility_excel_file()
        lp.nextbuttonone()
        lp.selectTogetherProcess()
        lp.nextbuttonone()
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
        lp.createMicroplan()

        driver.save_screenshot(".\\Screenshots\\createMP.png")
        driver.quit()
        

       