from selenium import webdriver
import allure
import pytest

def test_vwo_sample_selenium_3():
    driver_path = '/Users/pramod/Downloads/edge/msedgedriver'
    #additional step: when using selenium3 -> driver downloaded explicitly
    # browser and browser server too

    driver = webdriver.EdgeService(executable_path=driver_path)
    driver.get("https://app.vwo.com")