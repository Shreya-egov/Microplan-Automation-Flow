import datetime
import os
import random
import string
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException




class TestMPFlow:
    def __init__(self, driver):
        self.driver = driver
        
        self.username_field = (By.NAME, 'username')
        self.password_field = (By.NAME, 'password')
        
        self.country_dropdown = (By.CLASS_NAME, 'digit-dropdown-employee-select-wrap--elipses.false')
        self.login_button = (By.CLASS_NAME, 'digit-submit-bar.w-full')
        self.privacy_checkbox =(By.XPATH, "/html/body/div[1]/div/div/div/div/div/form/div/div[6]/div/div/div/div[1]/div/div")
        # self.privacy_checkbox =(By.CSS_SELECTOR, '.input.input-emp.undefined')
        self.setup_microplan_link = (By.CLASS_NAME,'digit-button-teritiary.medium')  # Update with actual XPath of the link
        # QAself.campaigntypedropdown = (By.XPATH, "//div[1]//div[1]//div[1]//form[1]//div[1]//div[2]//div[1]//div[1]//div[2]//div[2]//div[1]//input[1]")  # Update with actual XPath
        self.campaigntypedropdown = (By.XPATH, "//div[1]//div[1]//div[1]//form[1]//div[1]//div[2]//div[1]//div[1]//div[2]//div[2]//div[1]")  # Update with actual XPath
        # self.campaignstrategy = (By.CSS_SELECTOR, 'body > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > form:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(5) > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)') 
       
        self.campaignstrategy = (By.CSS_SELECTOR, 'body > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > form:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(5) > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)') 
        self.Bednetoption = (By.CSS_SELECTOR, 'body > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > form:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1)')
        self.H2Hoption = (By.CSS_SELECTOR, 'body > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > form:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(5) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)')
        self.nextbutton1 = (By.CLASS_NAME, "submit-bar")
        # self.nextbutton1 = (By.CSS_SELECTOR, "#root > div > div > div > div.main.digit-home-main > div.employee-app-wrapper.digit-home-app-wrapper > div > div > form > div.action-bar-wrap.actionBarClass.microplan-actionbar > button.submit-bar")
        self.microplan_name_field = (By.NAME, 'microplanName')
        self.popupbutton = (By.CLASS_NAME, "digit-button-secondary.large.campaign-type-alert-button")
        

       #boundaryselectionpage
        # self.dropdowncountry = (By.CSS_SELECTOR, '#root > div > div > div > div.main.digit-home-main > div.employee-app-wrapper.digit-home-app-wrapper > div > div.app-container.campaign > form > div.setup-campaign-card > div.employeeCard > div > div:nth-child(3) > div > div > div.digit-multiselectdropdown-wrap.selecting-boundaries-dropdown > div.digit-multiselectdropdown-master-active')
        self.dropdowncountry = (By.CSS_SELECTOR, 'body > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > form:nth-child(3) > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)')
        self.countryoption = (By.CSS_SELECTOR, '#jk-dropdown-unique > div > div > input'  )
        self.dropdownprovince = (By.XPATH, '//div[1]//div[1]//div[1]//form[1]//div[1]//div[3]//div[1]//div[2]//div[1]//div[1]//div[1]//div[1]')
        self.provinceoption = (By.CSS_SELECTOR, '#jk-dropdown-unique > div > div:nth-child(3)')
        self.bg1 = (By.CSS_SELECTOR, '#root > div > div > div > div.main.digit-home-main > div.employee-app-wrapper.digit-home-app-wrapper > div > div > form > div.setup-compaign-card > div.digit-card-component.selecting-boundary-card > div > div:nth-child(3) > h2')
        self.bg2 = (By.CLASS_NAME, 'digit-card-label boundary-selection-label')
        self.dropdowndistrict = (By.XPATH,"//*[@id='root']/div/div/div/div[3]/div[1]/div/div/form/div[1]/div[3]/div/div[3]/div/div/div[1]/div[1]")
        self.districtoption = (By.CLASS_NAME, 'digit-multiselectdropodwn-menuitem.nestedmultiselect.selectAll')
        self.dropdownpost = (By.CSS_SELECTOR, '#root > div > div > div > div.main.digit-home-main > div.employee-app-wrapper.digit-home-app-wrapper > div > div > form > div.setup-compaign-card > div.digit-card-component.selecting-boundary-card > div > div:nth-child(4) > div > div > div.digit-multiselectdropdown-wrap.selecting-boundaries-dropdown.nestedmultiselect')
        self.APoption = (By.CLASS_NAME, 'digit-multiselectdropodwn-menuitem.nestedmultiselect.selectAll')
        self.dropdownlocality = (By.XPATH, "/html/body/div[1]/div/div/div/div[3]/div[1]/div/div/form/div[1]/div[3]/div/div[5]/div/div/div[1]/div[1]")
        self.localityoption = (By.CLASS_NAME, "digit-multiselectdropodwn-menuitem.nestedmultiselect.selectAll")
        self.dropdownvillage = (By.XPATH, "/html/body/div[1]/div/div/div/div[3]/div[1]/div/div/form/div[1]/div[3]/div/div[6]/div/div/div[1]/div[1]")
        self.villageoption = (By.CLASS_NAME, "digit-multiselectdropodwn-menuitem.nestedmultiselect.selectAll")
        self.DownloadTemplate = (By.CLASS_NAME,'icon-label-container.secondary.large')
        # self.dropdownvillage = (By.XPATH, "")
        self.submit_button1 = (By.CSS_SELECTOR, "button[type='submit'] header")

       
        #fileupload
        self.fileinput = (By.ID, "file")
        self.popfilepath = '/home/shreya-kumar/Downloads/Population Template (DEMO).xlsx'
        self.Facfilepath = '/home/shreya-kumar/Downloads/Facility Template (DEMO).xlsx'

        #Assumptions
        self.next = (By.CLASS_NAME, 'digit-button-primary.large.previous-button')
        self.together = (By.XPATH, '//*[@id="root"]/div/div/div/div[3]/div[1]/div/div/form/div[1]/div[2]/div/div/div[2]/div[2]/span')
        self.Genassump1 = (By.NAME, 'AVERAGE_PEOPLE_IN_A_HOUSEHOLD')
        self.Genassump2 = (By.NAME, 'NO_OF_BEDNETS_PER_BALE')
        self.Genassump3 = (By.NAME, 'NO_OF_PEOPLE_PER_BEDNET')
        
        self.HRassump1 = (By.NAME, 'NO_OF_DAYS_FOR_HOUSEHOLD_REGISTRATION')
        self.HRassump2 = (By.NAME, 'NO_OF_BENEFICIARIES_TO_BE_REGISTERED_BY_A_HOUSEHOLD_REGISTRATION_TEAM_PER_DAY')
        self.HRassump3 = (By.NAME, 'NO_OF_MEMBERS_PER_HOUSEHOLD_REGISTRATION_TEAM')
        self.HRassump4 = (By.NAME, 'NO_OF_HOUSEHOLD_REGISTRATION_TEAMS_PER_MONITOR')
        self.HRassump5 = (By.NAME, 'NO_OF_MONITORS_PER_SUPERVISOR_FOR_HOUSEHOLD_REGISTRATION')

        self.commodities = (By.NAME, 'NO_OF_HOUSEHOLDS_PER_STICKER_ROLL')

        #Tagusers
        #NationalEstimationAprrover
        self.addNMEP = (By.CLASS_NAME, 'digit-button-label')
        self.assignNMP = (By.CLASS_NAME, 'sc-fzXfOw sc-fzXfOx.sc-fzXfOy fZeuVe rdt_TableCell')
        self.closeicon = (By.CLASS_NAME , 'popup-close-svg')

        #NationalFacilityAssigner
        self.addNFA = (By.CLASS_NAME, 'icon-label-container.secondary.large')
        self.assignfac = (By.ID, 'cell-6-undefined')
        #  self.closeicon = (By.CLASS_NAME , 'popup-close-svg')

        #NationalPopulationApprover
        self.contactnumber = (By.NAME, 'number')
        self.search = (By.CLASS_NAME, 'digit-button-primary.large')
        #createMicroplan
        self.createMPbutton = (By.CSS_SELECTOR, "button[type='submit'] header")
        self.createMicroplan1 = (By.CLASS_NAME, "digit-panel-message")
    
    
    def setusername(self, username):
        try:
            username_elem = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.username_field)
            )
            username_elem.clear()
            username_elem.send_keys(username)
        except Exception as e:
            print(f"Error setting username: {e}")

    def setpassword(self, password):
        try:
            password_elem = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.password_field)
            )
            password_elem.clear()
            password_elem.send_keys(password)
        except Exception as e:
            print(f"Error setting password: {e}")

    def setcountry(self, country_name):
        try:
            dropdown_element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.country_dropdown)
            )
            dropdown_element.click()

            options_xpath = '//*[@id="root"]/div/div/div/div/div/form/div/div[5]/div/div/div[1]/div/div/div'
            options = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, options_xpath))
            )
            
            for option in options:
                if option.text == country_name:
                    option.click()
                    break
        except Exception as e:
            print(f"Error selecting country: {e}")

    def dpp(self):
        try:
            dpp_button_elem = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.privacy_checkbox)
            )
            dpp_button_elem.click()
        except Exception as e:
            print(f"Error clicking dpp button: {e}")

    def login(self):
        try:
            login_button_elem = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.login_button)
            )
            login_button_elem.click()
        except Exception as e:
            print(f"Error clicking login button: {e}")

    def get_setup_microplan_element(self):
        try:
        # Wait for the 'Setup Microplan' element to be clickable and click on it
            setup_microplan_elem = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.setup_microplan_link)
            )
            setup_microplan_elem.click()

        # Wait for the campaign type dropdown to be clickable and click on it
            campaigntypedropdown_elem = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(self.campaigntypedropdown)
            )
            campaigntypedropdown_elem.click()

        # Wait for all options in the dropdown to be present
            # BEDNEToptions_CSS = 'body > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > form:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1)'
        
        # Wait for options to be loaded and obtain all the options
            options = WebDriverWait(self.driver, 15).until(
                EC.presence_of_all_elements_located(self.Bednetoption)
            )

        # Loop through the options and select the one with the correct text (e.g., "Bednet Campaign")
            for option in options:
                if option.text == 'Bednet Campaign':  # Replace with the exact text you want to match
                    option.click()
                break
            else:
                print("Option 'Bednet Campaign' not found in dropdown.")
                
                
        # Wait for the strategy type dropdown to be clickable and click on it
            campaignstrategy_elem = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(self.campaignstrategy)
            )
            campaignstrategy_elem.click()

        # Wait for all options in the dropdown to be present
            # H2H_CSS = 'body > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > form:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(5) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)'
        
        # Wait for options to be loaded and obtain all the options
            options = WebDriverWait(self.driver, 15).until(
                EC.presence_of_all_elements_located( self.H2Hoption)
            )

        # Loop through the options and select the one with the correct text (e.g., "Bednet Campaign")
            for option in options:
                if option.text == 'House-To-House':  # Replace with the exact text you want to match
                    option.click()
                break
            else:
                print("Option 'House-To-House' not found in dropdown.")

        except Exception as e:
            print(f"Error selecting option: {e}")
            
            
            
    

    def nextbuttonone(self):
        time.sleep(3)
        try:
            next1_button_elem = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(self.nextbutton1)
            )
            next1_button_elem.click()
        except Exception as e:
            print(f"Error clicking dpp button: {e}")     

    def nextbuttontwo(self):
        try:
            next1_button_elem = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(self.next)
            )
            next1_button_elem.click()
        except Exception as e:
            print(f"Error clicking dpp button: {e}")     

            time.sleep(3)        

    def set_unique_microplan_name(self):
        # Generate a unique campaign name
        timestamp = int(time.time())
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
        unique_name = f"BednetH2H_{timestamp}_{random_string}"

        try:
            name_field_elem = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.microplan_name_field)
            )
            name_field_elem.clear()
            name_field_elem.send_keys(unique_name)
            return unique_name
        except Exception as e:
            print(f"Error setting campaign name: {e}")
            
 
        
    def popprocceed(self):
        try:
            acceptpop= WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(self.popupbutton)

            )
            acceptpop.click()

        except Exception as e:
            print(f"Error accepting popup: {e}")

      

    def submit_campaign(self):
        try:
            submit_button_elem = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(self.submit_button)
            )
            submit_button_elem.click()
        except Exception as e:
            print(f"Error clicking submit button: {e}")

    def countrydropdown(self):
    #     # try:
        # Click the dropdown to show options
            countrydropdown_elem = WebDriverWait(self.driver, 30).until(
               EC.element_to_be_clickable(self.dropdowncountry)
            )
            countrydropdown_elem.click()

    #     # Wait for the options to become visible
    #         # coptions_xpath = '=//*[@id="jk-dropdown-unique"]/div/div/input'
        
            # coptions_css = '#jk-dropdown-unique > div > div > input'  
            options = WebDriverWait(self.driver, 20).until(
                EC.presence_of_all_elements_located(self.countryoption)
            )
            # coptions_xpath.click()

            if options:  # Check if the list is not empty
                 options[0].click()  # Click the first WebElement in the list
            else:
                raise Exception("Error selecting values from country dropdown")
            
            time.sleep(3)


    def provincedropdown(self):
        try:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 1.5);")  # Scroll to the middle of the page
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.dropdownprovince))  # Wait for the dropdown to be present

            # provincedropdown_element = WebDriverWait(self.driver, 10).until(
            # EC.presence_of_element_located(self.dropdownprovince)
            # )
            # self.driver.execute_script("arguments[0].scrollIntoView(true);", provincedropdown_element)
       
    
            provincedropdown_elem = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(self.dropdownprovince)
            )
            provincedropdown_elem.click()

        # Wait for the options container to be visible
            # poptions_css = '#jk-dropdown-unique > div > div:nth-child(3)'
          
            options_container = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(self.provinceoption)
            )
            options_container.click()

          

        except TimeoutException as e:
            print(f"Timeout while selecting values from province dropdown: {e}")
        except Exception as e:
            print(f"Error selecting values from province dropdown: {e}")

            time.sleep(3)
   
    def BG1click(self):
        try:
            bg1_elem = WebDriverWait(self.driver, 1).until(
                EC.element_to_be_clickable(self.bg1)
            )
            bg1_elem.click()
        except Exception as e:
            print(f"Error clicking submit button: {e}")

            time.sleep(3)
    
    def BG2click(self):
        try:
            bg1_elem = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.bg2)
            )
            bg1_elem.click()
        except Exception as e:
            print(f"Error clicking submit button: {e}")

    def districtdropdown(self):
        try:
            # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 1.5);")  # Scroll to the middle of the page
            # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.dropdowndistrict))  # Wait for the dropdown to be present
    
            districtdropdown_elem = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(self.dropdowndistrict)
            )
            districtdropdown_elem.click()

        # Wait for the options container to be visible
            # doptions_css = 'digit-multiselectdropodwn-menuitem.nestedmultiselect.selectAll'
          
            options_container = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(self.districtoption)
            )
            options_container.click()

            time.sleep(3)

        except TimeoutException as e:
            print(f"Timeout while selecting values from province dropdown: {e}")
        except Exception as e:
            print(f"Error selecting values from province dropdown: {e}")


    def APdropdown(self):
        try:
            APdropdown_elem = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(self.dropdownpost)
            )
            APdropdown_elem.click()

            # apoptions_css = 'digit-multiselectdropodwn-menuitem.nestedmultiselect.selectAll'  # Adjust based on the actual HTML
            apoptions = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(self.APoption)
            )
            apoptions.click()

            time.sleep(3)
            # for option in options:
            #     if option.text == APdrop:
            #         option.click()
            #         break
        except Exception as e:
            print(f"Error selecting value from dropdown: {e}")

            

    def Localitydropdown(self):
        try:
        # Click dropdown
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            Locdropdown_elem = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(self.dropdownlocality)
            )
            Locdropdown_elem.click()

        # Wait for options to be visible
            # locoptions_class = "digit-multiselectdropodwn-menuitem.nestedmultiselect.selectAll"  
            locoptions = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(self.localityoption)
            )

        # Click the option
            locoptions.click()

        except Exception as e:
            print(f"Error selecting value from dropdown: {e}")
        except Exception as e:
            print(f"Error selecting value from dropdown: {e}")

        time.sleep(3)

    def VillageDropdown(self):
        try:
        # Click dropdown
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            Villagedropdown_elem = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(self.dropdownvillage)
            )
            Villagedropdown_elem.click()

        # Wait for options to be visible
            # viloptions_class = "digit-multiselectdropodwn-menuitem.nestedmultiselect.selectAll"  
            viloptions = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(self.villageoption)
            )

        # Click the option
            viloptions.click()

        except Exception as e:
            print(f"Error selecting value from dropdown: {e}")
        except Exception as e:
            print(f"Error selecting value from dropdown: {e}")
        
        time.sleep(3)



    def upload_Pop_excel_file(self):
        try:

            # DownloadTemp = WebDriverWait(self.driver, 40).until(
            #     EC.element_to_be_clickable(self.DownloadTemplate)  # Adjust the selector
            # )

            # DownloadTemp.click()

            time.sleep(10)
        
            file_input = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(self.fileinput)  # Adjust the selector
            )

            time.sleep(10)

            # popfilepath = '/home/shreya-kumar/Downloads/Population Template (DEMO).xlsx'
            # Set the file path to the file input element
            file_input.send_keys(self.popfilepath)

            time.sleep(10)
            
        except Exception as e:
            print(f"Error uploading Target file: {e}")



    def upload_Facility_excel_file(self):
        try:
            
            time.sleep(10)
           

            file_input = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located(self.fileinput)  # Adjust the selector
            )

            # Facfilepath = '/home/shreya-kumar/Downloads/Facility Template (DEMO).xlsx'
            # Set the file path to the file input element
            file_input.send_keys(self.Facfilepath)

            time.sleep(10)
            
        except Exception as e:
            print(f"Error uploading Facility file: {e}")


    def selectTogetherProcess(self):
        try:
            togethercheckbox = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(self.together)
            )
            togethercheckbox.click()
        except Exception as e:
            print(f"Error clicking Together checkbox button: {e}")

            # time.sleep(5)

    def Genassumptions(self):
        try:
            Genassump1 = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(self.Genassump1)
            )
            Genassump1.clear()
            Genassump1.send_keys("4")

            time.sleep(3)

            Genassump2 = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.Genassump2)
            )
            Genassump2.clear()
            Genassump2.send_keys("10")

            time.sleep(3)

            Genassump3 = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.Genassump3)
            )
            Genassump3.clear()
            Genassump3.send_keys("2")

            time.sleep(3)


        except Exception as e:
            print(f"Error in adding Genassump: {e}")

    def HRassump(self):
      

        try:
            HRassump1 = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(self.HRassump1)
            )
            HRassump1.clear()
            HRassump1.send_keys("10")

            time.sleep(3)

            HRassump2 = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.HRassump2)
            )
            HRassump2.clear()
            HRassump2.send_keys("10")

            time.sleep(3)

            HRassump3 = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.HRassump3)
            )
            HRassump3.clear()
            HRassump3.send_keys("10")

            time.sleep(3)

            HRassump4 = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.HRassump4)
            )
            HRassump4.clear()
            HRassump4.send_keys("10")

            time.sleep(3)

            HRassump5 = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.HRassump5)
            )
            HRassump5.clear()
            HRassump5.send_keys("10")

            time.sleep(3)

        except Exception as e:
            print(f"Error in adding Genassump: {e}")


    def commodassump(self):
        time.sleep(5)
        try:
            commodassump = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(self.commodities)
            )
            commodassump.clear()
            commodassump.send_keys("10")

            time.sleep(3)


        except Exception as e:
            print(f"Error in adding Genassump: {e}")

          

    def tagNMP(self):
        time.sleep(5)
        try:
            addNPA = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.addNMEP)
            )
            addNPA.click()

            time.sleep(5)

            searcbynumber = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.contactnumber)
            )
            searcbynumber.clear()
            searcbynumber.send_keys("9578015962")

            time.sleep(5)

            search = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.search)
            )
            search.click()

            time.sleep(5)

            assignpa = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(self.assignfac)
            )
            assignpa.click()

            time.sleep(5)

            closepopup = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(self.closeicon)
            )
            closepopup.click()

            time.sleep(5)

        except Exception as e:
                print(f"Error adding NMP: {e}")

    def tagNFA(self):
        time.sleep(3)
        try:
            addNPA = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.addNFA)
            )
            addNPA.click()

            time.sleep(5)

            searcbynumber = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.contactnumber)
            )
            searcbynumber.clear()
            searcbynumber.send_keys("9578012345")

            time.sleep(5)

            search = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.search)
            )
            search.click()

            time.sleep(5)

            assignpa = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(self.assignfac)
            )
            assignpa.click()

            time.sleep(5)

            closepopup = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(self.closeicon)
            )
            closepopup.click()

            time.sleep(5)

        except Exception as e:
                print(f"Error adding NPA: {e}")

    def tagNPA(self):
        time.sleep(3)
        try:
            addNPA = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.addNFA)
            )
            addNPA.click()

            time.sleep(5)

            searcbynumber = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.contactnumber)
            )
            searcbynumber.clear()
            searcbynumber.send_keys("9578012362")

            time.sleep(5)

            search = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.search)
            )
            search.click()

            time.sleep(5)

            assignpa = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(self.assignfac)
            )
            assignpa.click()

            time.sleep(5)

            closepopup = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(self.closeicon)
            )
            closepopup.click()

            time.sleep(5)

        except Exception as e:
                print(f"Error adding NPA: {e}")



    
    # def createMicroplan(self):

    #     # createnbutton = WebDriverWait(self.driver, 10).until(
    #     #     EC.element_to_be_clickable(self.createMPbutton)

    #     # )

    #     # createnbutton.click()
    
    # # Wait for the element containing the success message to be present
    #     createcampaign_element = WebDriverWait(self.driver, 15).until(
    #         EC.presence_of_element_located(self.createMicroplan1)
    #     )
    
    # # Retrieve the text from the element
    #     actual_text = createcampaign_element.text

    # # Define the expected text
    #     expected_text = "Microplan setup completed!"

    # # Verify the text
    #     assert actual_text == expected_text, f"Text verification failed: Expected '{expected_text}', but got '{actual_text}'"   
    #     print("Text verification passed.")
         
 
    def createMicroplan(self):

        try:
            # Wait for the element containing the success message to be present
            createcampaign_element = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(self.createMicroplan1)
            )
        
            # Retrieve the text from the element
            actual_text = createcampaign_element.text
        
            # Define the expected text
            expected_text = "Microplan setup completed!"
        
            # Verify the text
            assert actual_text == expected_text, f"Text verification failed: Expected '{expected_text}', but got '{actual_text}'"
            print("Text verification passed.")
        
        except Exception as e:
            # If there's any exception or failure, capture a screenshot for debugging
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            screenshot_folder = "./Screenshots"
            if not os.path.exists(screenshot_folder):
                os.makedirs(screenshot_folder)

            screenshot_filename = os.path.join(screenshot_folder, f"createMicroplan_{timestamp}.png")
            self.driver.save_screenshot(screenshot_filename)
            print(f"Screenshot saved at: {screenshot_filename}")
            print(f"Error: {str(e)}")
            raise e 
 
    
    
    
    

 
            


    
    
    
    
    
    

 
            

    
    
    

 
            


    
    
    
    
    
    

 
            
