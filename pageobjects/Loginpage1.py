import datetime
import random
import string
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys



class Loginpage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.NAME, 'username')
        self.password_field = (By.NAME, 'password')
        
        self.country_dropdown = (By.CSS_SELECTOR, '#root > div > div > div > div > div > form > div > div:nth-child(6) > div > div > div.digit-dropdown-employee-select-wrap > div > input')
        self.login_button = (By.CSS_SELECTOR, '#root > div > div > div > div > div > form > div > button')
        self.privacy_checkbox = (By.CSS_SELECTOR, '#root > div > div > div > div > div > form > div > div:nth-child(7) > div > div > div.digit-privacy-checkbox > div > div')
        self.setup_campaign_link = (By.CSS_SELECTOR,'#root > div > div > div > div.main.digit-home-main > div.employee-app-wrapper.digit-home-app-wrapper > div > div > div > div:nth-child(1) > div > div.body > div > span:nth-child(1) > a')  # Update with actual XPath of the link
        self.campaigntypedropdown = (By.CSS_SELECTOR, '#root > div > div > div > div.main.digit-home-main > div.employee-app-wrapper.digit-home-app-wrapper > div > div.app-container.campaign > form > div.employeeCard.setup-campaign-card > div.label-field-pair > div > div > div.campaign-type-wrapper > div > div > input')  # Update with actual XPath
        self.IRStypedropdown_options = (By.XPATH, '//*[@id="jk-dropdown-unique"]/div[3]/div/div/span') 
        self.nextbutton1 = (By.CSS_SELECTOR, '#root > div > div > div > div.main.digit-home-main > div.employee-app-wrapper.digit-home-app-wrapper > div > div.app-container.campaign > form > div.action-bar-wrap.actionBarClass > button > header')
        self.campaign_name_field = (By.CSS_SELECTOR, '#root > div > div > div > div.main.digit-home-main > div.employee-app-wrapper.digit-home-app-wrapper > div > div.app-container.campaign > form > div.employeeCard.setup-campaign-card > div.label-field-pair > div.digit-field > div.digit-text-input-field.text > div > input')
        self.submit_button = (By.CSS_SELECTOR, '#root > div > div > div > div.main.digit-home-main > div.employee-app-wrapper.digit-home-app-wrapper > div > div.app-container.campaign > form > div.action-bar-wrap.actionBarClass > button.submit-bar')

        #boundaryselectionpage
        # self.dropdowncountry = (By.CSS_SELECTOR, '#root > div > div > div > div.main.digit-home-main > div.employee-app-wrapper.digit-home-app-wrapper > div > div.app-container.campaign > form > div.setup-campaign-card > div.employeeCard > div > div:nth-child(3) > div > div > div.digit-multiselectdropdown-wrap.selecting-boundaries-dropdown > div.digit-multiselectdropdown-master-active')
        self.dropdowncountry = (By.CSS_SELECTOR, '#root > div > div > div > div.main.digit-home-main > div.employee-app-wrapper.digit-home-app-wrapper > div > div.app-container.campaign > form > div.setup-campaign-card > div.employeeCard > div > div:nth-child(3) > div > div > div.digit-multiselectdropdown-wrap.selecting-boundaries-dropdown')
        self.dropdownprovince = (By.CSS_SELECTOR, '#root > div > div > div > div.main.digit-home-main > div.employee-app-wrapper.digit-home-app-wrapper > div > div.app-container.campaign > form > div.setup-campaign-card > div.employeeCard > div > div:nth-child(4) > div > div > div.digit-multiselectdropdown-wrap.selecting-boundaries-dropdown.nestedmultiselect > div')
        self.bg1 = (By.CSS_SELECTOR, '#root > div > div > div > div.main.digit-home-main > div.employee-app-wrapper.digit-home-app-wrapper > div > div.app-container.campaign > form > div.setup-campaign-card > div.employeeCard > div > div:nth-child(5) > h2')
        self.bg2 = (By.CSS_SELECTOR, '#root > div > div > div > div.main.digit-home-main > div.employee-app-wrapper.digit-home-app-wrapper > div > div.app-container.campaign > form > div.setup-campaign-card > div.employeeCard > div > div:nth-child(6) > h2')
        self.dropdowndistrict = (By.XPATH, '//*[@id="root"]/div/div/div/div[3]/div[1]/div/div[2]/form/div[1]/div[2]/div/div[3]/div/div/div[1]/div')
        self.dropdownpost = (By.CSS_SELECTOR, '#root > div > div > div > div.main.digit-home-main > div.employee-app-wrapper.digit-home-app-wrapper > div > div.app-container.campaign > form > div.setup-campaign-card > div.employeeCard > div > div:nth-child(6) > div > div > div.digit-multiselectdropdown-wrap.selecting-boundaries-dropdown.nestedmultiselect > div')
        self.submit_button1 = (By.CSS_SELECTOR, "button[type='submit'] header")

        #campaignDateSelection
        self.startdate = (By.CSS_SELECTOR, "input[placeholder='Start Date']")
        self.enddate = (By.CSS_SELECTOR, "input[placeholder='End Date']")
        self.submit_button2 = (By.CSS_SELECTOR, "button[type='submit'] header")

        #cycledateseelction
        self.cycle1startdate = (By.CSS_SELECTOR, "#root > div > div > div > div.main.digit-home-main > div.employee-app-wrapper.digit-home-app-wrapper > div > div.app-container.campaign > form > div.setup-campaign-card > div:nth-child(6) > div > div > div:nth-child(1) > div > input")
        self.cycle1enddate = (By.CSS_SELECTOR, "input[placeholder='End date']")
       
        #fileupload
        self.cancelpopup = (By.CSS_SELECTOR, "div[class='digit-popup-footer-buttons '] div[class='icon-label-container secondary large'] h2[class='digit-button-label']")
        self.browsefile = (By.CSS_SELECTOR, ".browse-text")
        self.fileinput = (By.CSS_SELECTOR, "#root > div > div > div > div.main.digit-home-main > div.employee-app-wrapper.digit-home-app-wrapper > div > div.app-container.campaign > form > div.setup-campaign-card > div.employeeCard > label > input[type=file]")

        #createcampaign
        self.createcampaign = (By.CSS_SELECTOR, "#root > div > div > div > div.main.digit-home-main > div.employee-app-wrapper.digit-home-app-wrapper > div > div.app-container.campaign > div.digit-panelcard-wrap > div.digit-panelcard-header > div > div.digit-panel-message-wrapper.success > div.digit-panel-message")
    
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

    def get_setup_campaign_element(self):
        try:
            setup_campaign_elem = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.setup_campaign_link)
            )
            setup_campaign_elem.click()
        except Exception as e:
            print(f"Error finding setup campaign element: {e}")
            
    def select_campaigntype_from_dropdown(self, IRSCT_name):
        try:
            # Open the dropdown
            campaigntypedropdown_elem = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(self.campaigntypedropdown)
            )
            campaigntypedropdown_elem.click()

            IRSoptions_CSS = 'body > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > form:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)'
            options = WebDriverWait(self.driver, 15).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, IRSoptions_CSS))
            )
            
            for option in options:
                if option.text == IRSCT_name:
                    option.click()
                    break
        except Exception as e:
            print(f"Error selecting IRS options: {e}")

    def nextbuttonone(self):
        try:
            next1_button_elem = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(self.nextbutton1)
            )
            next1_button_elem.click()
        except Exception as e:
            print(f"Error clicking dpp button: {e}")            

    def set_unique_campaign_name(self):
        # Generate a unique campaign name
        timestamp = int(time.time())
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
        unique_name = f"IRSCampaign_{timestamp}_{random_string}"

        try:
            name_field_elem = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.campaign_name_field)
            )
            name_field_elem.clear()
            name_field_elem.send_keys(unique_name)
            return unique_name
        except Exception as e:
            print(f"Error setting campaign name: {e}")

    def submit_campaign(self):
        try:
            submit_button_elem = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(self.submit_button)
            )
            submit_button_elem.click()
        except Exception as e:
            print(f"Error clicking submit button: {e}")

    def countrydropdown(self, countrydrop):
    #     # try:
        # Click the dropdown to show options
            countrydropdown_elem = WebDriverWait(self.driver, 10).until(
               EC.element_to_be_clickable(self.dropdowncountry)
            )
            countrydropdown_elem.click()

    #     # Wait for the options to become visible
    #         # coptions_xpath = '=//*[@id="jk-dropdown-unique"]/div/div/input'
        
            coptions_css = '#jk-dropdown-unique > div > div > input'  
            options = WebDriverWait(self.driver, 15).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, coptions_css))
            )
            # coptions_xpath.click()

            if options:  # Check if the list is not empty
                 options[0].click()  # Click the first WebElement in the list
            else:
                raise Exception("Error selecting values from country dropdown")

            # for option in options:
            #     if option.text == countrydrop:
            #         option.click()
            #         break
            #     except Exception as e:
            #         print(f"Error selecting country options: {e}")

    #     # Iterate over the options and select checkboxes
    #         # for option in options:
    #         #     # try:
    #         #     # Locate the checkbox and label within each option
    #         #         checkbox_xpath = '//*[@id="jk-dropdown-unique"]/div/div/div[1]'  # Adjust this XPath based on your HTML structure
    #         #         label_xpath = '//*[@id="jk-dropdown-unique"]/div/div/div[2]'  # Adjust this XPath based on your HTML structure

    #         #         checkbox = option.find_element(By.XPATH, checkbox_xpath)
    #         #         label = option.find_element(By.XPATH, label_xpath)

    #         #     # Select the checkbox if it matches any of the desired country names
    #         #         # if label.text.strip() in countrydrop_list and not checkbox.is_selected():
    #         #         checkbox.click()
    #             # except Exception as e:
    #             #     print(f"Error interacting with option: {e}")

            # except Exception as e:
            #     print(f"Error selecting values from country dropdown: {e}")

    def provincedropdown(self, provincedrop):
        try:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 1.5);")  # Scroll to the middle of the page
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.dropdownprovince))  # Wait for the dropdown to be present

            # provincedropdown_element = WebDriverWait(self.driver, 10).until(
            # EC.presence_of_element_located(self.dropdownprovince)
            # )
            # self.driver.execute_script("arguments[0].scrollIntoView(true);", provincedropdown_element)
       
    
            provincedropdown_elem = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(self.dropdownprovince)
            )
            provincedropdown_elem.click()

        # Wait for the options container to be visible
            poptions_css = '#jk-dropdown-unique > div > div:nth-child(4)'
          
            options_container = WebDriverWait(self.driver, 16).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, poptions_css))
            )
            options_container.click()

            # more_options_available = True

            # while more_options_available:
            # # Retrieve all options within the visible container
            #     options = options_container.find_elements(By.CSS_SELECTOR, '#jk-dropdown-unique > div > div:nth-child(4)')

            #     new_options_loaded = False

            #     for option in options:
            #         try:
            #         # Locate the checkbox and label within each option
            #             checkbox_css = '#jk-dropdown-unique > div > div:nth-child(4) > div.digit-multiselectdropodwn-custom-checkbox'  # Adjust this XPath based on your HTML structure
            #             label_css = '#jk-dropdown-unique > div > div:nth-child(4) > div.option-des-container'  # Adjust this XPath based on your HTML structure

            #             checkbox = option.find_element(By.CSS_SELECTOR, checkbox_css)
            #             label = option.find_element(By.CSS_SELECTOR, label_css)

            #         # Select the checkbox if it matches any of the desired province names
            #             if label.text.strip() in provincedrop and not checkbox.is_selected():
            #                 checkbox.click()
            #                 new_options_loaded = True

                    # except NoSuchElementException as e:
                    #     print(f"Element not found: {e}")
                    # except Exception as e:
                    #     print(f"Error interacting with option: {e}")

            # # Scroll to the bottom of the options container
            #     self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", options_container)
            
            # Check if there are more options to load
                # try:
                # # Wait briefly and check for new options
                #     WebDriverWait(self.driver, 1).until(
                #         EC.presence_of_all_elements_located((By.XPATH, '//*[@id="jk-dropdown-unique"]/div/div[4]/input'))  # Adjust based on the HTML structure
                #     )
                # except TimeoutException:
                # # Break the loop if no new options are found
                #     more_options_available = False
                
                # if not new_options_loaded:
                #     more_options_available = False

        except TimeoutException as e:
            print(f"Timeout while selecting values from province dropdown: {e}")
        except Exception as e:
            print(f"Error selecting values from province dropdown: {e}")
   
    def BG1click(self):
        try:
            bg1_elem = WebDriverWait(self.driver, 1).until(
                EC.element_to_be_clickable(self.bg1)
            )
            bg1_elem.click()
        except Exception as e:
            print(f"Error clicking submit button: {e}")
    
    def BG2click(self):
        try:
            bg1_elem = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.bg2)
            )
            bg1_elem.click()
        except Exception as e:
            print(f"Error clicking submit button: {e}")

    def districtdropdown(self, districtdrop):
        try:
            # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 1.5);")  # Scroll to the middle of the page
            # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.dropdowndistrict))  # Wait for the dropdown to be present
    
            districtdropdown_elem = WebDriverWait(self.driver, 16).until(
                EC.element_to_be_clickable(self.dropdowndistrict)
            )
            districtdropdown_elem.click()

        # Wait for the options container to be visible
            doptions_css = '#jk-dropdown-unique > div > div:nth-child(3)'
          
            options_container = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, doptions_css))
            )
            options_container.click()

        except TimeoutException as e:
            print(f"Timeout while selecting values from province dropdown: {e}")
        except Exception as e:
            print(f"Error selecting values from province dropdown: {e}")

    def APdropdown(self, APdrop):
        try:
            APdropdown_elem = WebDriverWait(self.driver, 16).until(
                EC.element_to_be_clickable(self.dropdownpost)
            )
            APdropdown_elem.click()

            apoptions_css = '#jk-dropdown-unique > div > div:nth-child(3)'  # Adjust based on the actual HTML
            apoptions = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, apoptions_css))
            )
            apoptions.click()
            # for option in options:
            #     if option.text == APdrop:
            #         option.click()
            #         break
        except Exception as e:
            print(f"Error selecting value from dropdown: {e}")

    def submit_boundary1(self):
        try:
            submit_button_elem1 = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(self.submit_button1)
            )
            submit_button_elem1.click()
        except Exception as e:
            print(f"Error clicking boundary selection submit button: {e}")

    def selectStartDate(self):
        try:
            startdate_elem1 = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.startdate)
            )
            startdate_elem1.click()

            sdate_value = '2024-09-17'  # Replace with the desired date
            actions = ActionChains(self.driver)
            actions.send_keys(sdate_value).send_keys(Keys.RETURN).perform()

            time.sleep(2)
           
        except Exception as e:
            print(f"Error clicking start date field: {e}")

    def selectEndDate(self):
        try:
            enddate_elem1 = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.enddate)
            )
            enddate_elem1.click()

            edate_value = '2024-09-19'  # Replace with the desired date\
            actions = ActionChains(self.driver)
            actions.send_keys(edate_value).send_keys(Keys.RETURN).perform()

            
            time.sleep(2)
            # enddate_elem1.send_keys(edate_value)
        except Exception as e:
            print(f"Error clicking end date field: {e}")

    def submit_dates1(self):
        try:
            submit_button_elem2 = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(self.submit_button2)
            )
            submit_button_elem2.click()
        except Exception as e:
            print(f"Error clicking campaigndates submit button: {e}")

    def cycle1selectStartDate(self):
        try:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 1.5);")  # Scroll to the middle of the page
            # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.cycle1startdate))  # 
            time.sleep(2)
            cstartdate_elem1 = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.cycle1startdate)
            )
            cstartdate_elem1.click()

            sdate_value = '2024-09-17'  # Replace with the desired date
            actions = ActionChains(self.driver)
            actions.send_keys(sdate_value).send_keys(Keys.RETURN).perform()

            time.sleep(2)
           
        except Exception as e:
            print(f"Error clicking cycle start date field: {e}")

    def cycle1selectEndDate(self):
        try:
            
            cenddate_elem1 = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.cycle1enddate)
            )
            cenddate_elem1.click()

            edate_value = '2024-09-19'  # Replace with the desired date\
            actions = ActionChains(self.driver)
            actions.send_keys(edate_value).send_keys(Keys.RETURN).perform()

            
            time.sleep(2)
            # enddate_elem1.send_keys(edate_value)
        except Exception as e:
            print(f"Error clicking end date field: {e}")

    def upload_Target_excel_file(self):
        try:
            
            Cancelpopup_elem1 = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.cancelpopup)
            )
            Cancelpopup_elem1.click()

            time.sleep(5)

            file_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.fileinput)  # Adjust the selector
            )

            filepath = '/home/shreya/Downloads/Target Template (1).xlsx'
            # Set the file path to the file input element
            file_input.send_keys(filepath)

            time.sleep(10)
            
        except Exception as e:
            print(f"Error uploading Target file: {e}")

    def upload_Facility_excel_file(self):
        try:
            
            Cancelpopup_elem1 = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.cancelpopup)
            )
            Cancelpopup_elem1.click()

            time.sleep(5)

            file_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.fileinput)  # Adjust the selector
            )

            filepath = '/home/shreya/Downloads/Facility Template (1).xlsx'
            # Set the file path to the file input element
            file_input.send_keys(filepath)

            time.sleep(10)
            
        except Exception as e:
            print(f"Error uploading Facility file: {e}")

    def upload_User_excel_file(self):
        try:
            
            Cancelpopup_elem1 = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.cancelpopup)
            )
            Cancelpopup_elem1.click()

            time.sleep(5)

            file_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.fileinput)  # Adjust the selector
            )

            filepath = '/home/shreya/Downloads/User Template (2).xlsx'
            # Set the file path to the file input element
            file_input.send_keys(filepath)

            time.sleep(10)
            
        except Exception as e:
            print(f"Error uploading User file: {e}")

    def createcampaignsuccessfully(self):
    # Wait for the element containing the success message to be present
        createcampaign_element = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(self.createcampaign)
        )
    
    # Retrieve the text from the element
        actual_text = createcampaign_element.text

    # Define the expected text
        expected_text = "Campaign data recorded successfully!"

    # Verify the text
        assert actual_text == expected_text, f"Text verification failed: Expected '{expected_text}', but got '{actual_text}'"   
        print("Text verification passed.")


    
    
    
    
    

 
            


    
    
    
    
    
    

 
            
