**Microplan Automation Framework**
This repository contains a test automation framework for testing the Microplan application using Selenium WebDriver and Python. The framework follows the Page Object Model (POM) design pattern and includes various utilities to manage configurations and read test data.

**Features**
Modular and Scalable: The framework is designed using the Page Object Model (POM) pattern, keeping the test scripts clean, reusable, and easy to maintain.

Dynamic Test Data: Utilities such as ReadConfig read configurations from external files (e.g., .ini or .properties files), enabling dynamic test execution with different data sets.

Extensive Test Coverage: Covers end-to-end test flows like logging into the application, navigating through the system, and performing actions like creating Microplans.

Allure Reporting: Generates detailed, visually appealing reports using Allure to visualize test results and provide insights into the test execution.

**Project Structure**
The project is organized as follows:

Microplan-Automation-Flow/
├── config/
│   └── config.ini                # Application configurations (URL, credentials, etc.)
├── pageobjects/
│   ├── __init__.py
│   └── Microplan.py              # Page Object for Microplan flow
├── testCases/
│   ├── __init__.py
│   ├── setupMicroplan.py         # The test case for the complete Microplan flow
│   └── conftest.py               # Pytest configuration
├── utilities/
│   ├── __init__.py
│   ├── readProperties.py         # Utility to read configurations from external files           
└── README.md                     # Project documentation
**Key Components**
Config Folder: Contains the config.ini file with necessary configuration details like the application URL, username, password, and other properties.

Page Objects: Contains the page object classes representing various pages and actions in the application.

Test Cases: Contains the main test files for specific test flows.

Utilities: Contains helper functions like reading configurations (readProperties.py).

**Requirements**
Before running the tests, ensure that you have the following installed:

Python 3.7+

Selenium WebDriver

Allure (for reporting)

Pytest (for test execution)

You can install these dependencies by creating a virtual environment and installing the required packages.

**Steps to Set Up**
Clone the repository:

git clone https://github.com/yourusername/Microplan-Automation-Flow.git
cd Microplan-Automation-Flow
Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
Install required packages:

You can use requirements.txt to manage dependencies (if not already created, you can manually install them):


**Running the Tests**
To execute the tests, use the following command:

pytest testCases/test_complete_flow.py --alluredir=allure-results
This command will:

Execute the test cases in testCases/test_complete_flow.py.

Generate the Allure results in the allure-results folder.

**Generating Allure Report**
If you have Allure Report Viewer installed, you can view the report by running:

allure serve allure-results
This will open a local server and display the Allure report in your browser.

Directory and File Overview
testCases/test_complete_flow.py: Contains the test logic for performing an end-to-end Microplan creation flow.

utilities/readProperties.py: Utility to read configuration values from the config.ini file and provide them to the test scripts.

pageobjects/Microplan.py: Page Object class that represents the elements and actions related to Microplan creation.

conftest.py: Pytest configuration file that defines fixtures, hooks, and setup/teardown logic for the test environment.

**Conclusion**
This framework allows you to automate the testing of the Microplan application, ensuring that each part of the application works correctly from login to creating Microplans. By following the Page Object Model and separating the configuration, utilities, and test logic, the framework remains flexible, scalable, and easy to maintain.

