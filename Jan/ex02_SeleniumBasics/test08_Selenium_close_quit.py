from selenium import webdriver
import allure
import pytest
import time

#1. close() -> `Closes the current window.`
#2. quit() -> `Quits the driver and closes every associated window.`



def test_katalon_firefox():
    driver = webdriver.Firefox()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    time.sleep(10)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"
    #driver.close() # current tab
    driver.quit()  # closes entire window and all its tabs.