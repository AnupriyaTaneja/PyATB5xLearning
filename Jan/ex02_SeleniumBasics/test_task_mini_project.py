from selenium import webdriver
import allure
import pytest
import time

def test_mini_project():
    driver = webdriver.Chrome()
    driver.get("https://demo.us.espocrm.com/")
    print(driver.title)
    assert driver.title == "EspoCRM Demo"
    print(driver.current_url)
    assert driver.current_url == "https://demo.us.espocrm.com/"
    time.sleep(15)