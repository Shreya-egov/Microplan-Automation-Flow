Microplan Automation Framework
This repository contains a test automation framework for testing the Microplan application using Selenium WebDriver and Python. The framework follows the Page Object Model (POM) design pattern and includes various utilities to manage configurations and reading test data.

Features
Modular and Scalable: The framework is designed using the Page Object Model (POM) pattern to keep the test scripts clean and easy to maintain.

Dynamic Test Data: Utilities such as ReadConfig are used to read configurations from external files (like .ini or .properties files).

Extensive Test Coverage: Covers end-to-end flows like logging into the application, navigating through the system, and performing actions like creating Microplans.

Allure Reporting: Provides detailed reports using Allure to visualize test results.

Project Structure
The project is organized as follows:

bash
Copy
Microplan-Automation-Flow/
├── config/
│   └── config.ini                # Application configurations (URL, credentials, etc.)
├── pageobjects/
│   ├── __init__.py
│   └── Microplan.py              # Page Object for Microplan flow
├── testCases/
│   ├── __init__.py
│   ├── setupMicroplan.py     # The test case for the complete Microplan flow
│   └── conftest.py               # Pytest configuration
├── utilities/
│   ├── __init__.py
│   ├── readProperties.py         # Utility to read configurations from external files           
└── README.md                     # Project documentation

Key Components:
Config Folder: Contains the config.ini file with necessary configuration details like the application URL, username, password, and other properties.

Page Objects: This folder contains the page object classes, which represent the different pages of the application.

Test Cases: The folder contains the main test case files. Each file corresponds to a specific test flow.

Utilities: Contains helper functions such as reading configurations (readProperties.py).


Requirements
Before running the tests, make sure you have the following installed:

Python 3.7+

Selenium WebDriver

Allure (for reporting)

Pytest (for test execution)



Clone this repository:


git clone https://github.com/yourusername/Microplan-Automation-Flow.git
cd Microplan-Automation-Flow
Create and activate a virtual environment:


python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate


This file should include all necessary libraries, such as:

ini
Copy
pytest==8.3.5
selenium==4.x.x
allure-pytest==2.13.5
Configuration
The configuration details like URL, username, password, and other application-specific values are stored in the config/config.ini file. Here's an example of how it might look:


Running the Tests
To run the tests, execute the following command:


pytest testCases/test_complete_flow.py --alluredir=allure-results
This command will:

Execute the test cases.

Generate the Allure results in the allure-results folder.

If you have the Allure report viewer installed, you can generate the report as follows:


allure serve allure-results
This will open a local server and display the Allure report in your browser.



Directory and File Overview
testCases/test_complete_flow.py: This file contains the test logic for performing an end-to-end Microplan creation flow.

utilities/readProperties.py: A utility that reads the configuration values from the config.ini file and makes them available for test scripts.

pageobjects/Microplan.py: Page object class representing the elements and actions for creating a Microplan.

conftest.py: The conftest.py file contains Pytest configuration such as fixture setups and other test configurations. This file runs before the tests to set up the testing environment.

Conclusion
This framework allows you to automate the testing of the Microplan application, ensuring that each part of the application works correctly from login to creating Microplans. By using the Page Object Model and separating the configuration, utilities, and test logic, the framework remains flexible, scalable, and easy to maintain.

Contribution
If you'd like to contribute to this project, please fork the repository, make changes, and submit a pull request.