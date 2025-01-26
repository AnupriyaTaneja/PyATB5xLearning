
from selenium import webdriver
import allure
import pytest

@allure.title("Verify that the title of vwo.com is expected.")
def test_vwo_sample():
    driver = webdriver.Edge()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    #if "CURA Healthcare Service" in driver.page_source:
    if "PURA Healthcare Service" in driver.page_source:

        print("Text Found!!, Test Case Passed!")
    else:
        print("Text not found on the page")
        pytest.fail("Text not found on the page")

    # Python interpreter is closing the browser after reading source code for each test
