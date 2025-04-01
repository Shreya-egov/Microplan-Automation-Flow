from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def setup():
    # Specify the path to your ChromeDriver
    driver_path = '/home/shreya-kumar/Downloads/chromedriver-linux64/chromedriver'  # Update this path

    # Create a Service object and initialize the WebDriver with the Service object
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service)

    # Maximize the window to ensure elements are visible
    driver.maximize_window()

    # Optionally, set implicit wait time to wait for elements to load
    driver.implicitly_wait(10)  # Wait up to 10 seconds for elements to appear
    
    try:
        # Yield the WebDriver to the test
        yield driver
    finally:
        # Cleanup / Teardown: Quit the driver after the test
        driver.quit()  # Ensures the driver quits regardless of any test failure
