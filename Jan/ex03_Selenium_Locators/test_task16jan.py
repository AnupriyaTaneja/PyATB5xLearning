import allure
import pytest
import time

from dotenv import load_dotenv
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


@allure.title("Task1 - Test Mini Project Espo CRM")
@allure.description("TC1 - Verify user is able to click on login button")
@pytest.mark.smoke

def test_login_button():
    chrome_options = Options()
    testdriver = webdriver.Chrome(chrome_options)
    testdriver.get("https://demo.us.espocrm.com/")
    time.sleep(5)

    testdriver.find_element(By.ID, "field-userName")
    testdriver.sendkeys("Administrator")

#     < select
#     name = "username"
#     value = "admin"
#     id = "field-userName"
#
#     class ="form-control" >
#
#     < option
#     value = "admin"
#     selected = "" > Administrator < / option >
#
# < / select >

    testdriver.find_element(By.ID, "field-language")
    testdriver.sendkeys("English (US)")

    #< select
    #class ="form-control" id="field-language" > < option value="en_US" > English (US) < / option >
    # < option value="ar_AR" > Arabic < / option > < option value="bg_BG" > Bulgarian < / option >
    # < option value="en_GB" selected="" > English (UK) < / option > < option value="es_MX" >
    # Spanish (Mexico) < / option > < option value="cs_CZ" > Czech < / option >
    # < option value="da_DK" > Danish < / option > < option value="de_DE" > German < / option >
    # < option value="es_ES" > Spanish (Spain) < / option > < option value="hr_HR" > Croatian < / option >
    # < option value="hu_HU" > Hungarian < / option > < option value="fa_IR" > Persian < / option >
    # < option value="fr_FR" > French (France) < / option > < option value="id_ID" > Indonesian < / option >
    # < option value="it_IT" > Italian < / option > < option value="lt_LT" > Lithuanian < / option >
    # < option value="lv_LV" > Latvian < / option > < option value="nb_NO" > Norwegian Bokmål < / option >
    # < option value="nl_NL" > Dutch < / option > < option value="th_TH" > Thai < / option >
    # < option value="tr_TR" > Turkish < / option > < option value="sk_SK" > Slovak < / option >
    # < option value="sl_SI" > Slovene < / option > < option value="sr_RS" > Serbian < / option >
    # < option value="sv_SE" > Swedish < / option > < option value="ro_RO" > Romanian < / option >
    # < option value="ru_RU" > Russian < / option > < option value="pl_PL" > Polish < / option >
    # < option value="pt_BR" > Portuguese (Brazil) < / option > < option value="pt_PT" > Portuguese (Portugal)
    # < / option >
    # < option value="uk_UA" > Ukrainian < / option > < option value="vi_VN" > Vietnamese < / option >
    # < option value="zh_CN" > Simplified Chinese (China) < / option >
    # < option value="zh_TW" > Traditional Chinese (Taiwan) < / option >
    # < / select >

    testdriver.find_element(By.ID, "btn-login").click()
    time.sleep(5)
    #Login button html code
    #<button type="submit" class="btn btn-primary btn-s-wide" id="btn-login">Login</button>

    assert testdriver.current_url == "https://demo.us.espocrm.com/?l=en_US"
    testdriver.quit()

    print("Login button clicked")
    print("TC1 passed")


@allure.title("Task - Test2 Mini Project Espo CRM")
@allure.description("TC2 - Verify user is able to click on Advance Pack link")
@pytest.mark.smoke

def test_advance_pack():
    chrome_options = Options()
    testdriver = webdriver.Chrome(chrome_options)
    testdriver.get("https://demo.us.espocrm.com/")
    #<a href="https://www.espocrm.com/extensions/advanced-pack/" target="_blank">Advanced Pack</a>
    adv_pack = testdriver.find_element(By.XPATH, "//a[@href='https://www.espocrm.com/extensions/advanced-pack/']")
    adv_pack.click()
    time.sleep(5)

    #print(testdriver.current_url)

   # assert testdriver.current_url == "https://www.espocrm.com/extensions/advanced-pack/"
    print("TC2 passed")


@allure.title("Task - Test3 Mini Project Espo CRM")
@allure.description("TC3 - Verify user is able to click on Sales Pack link")
@pytest.mark.smoke
def test_sales_pack():
    chrome_options = Options()
    testdriver = webdriver.Chrome(chrome_options)
    testdriver.get("https://demo.us.espocrm.com/")
    testdriver.find_element(By.LINK_TEXT, "Sales Pack").click()
    print("TC3 passed")

    #assert testdriver.current_url == "https://www.espocrm.com/extensions/sales-pack/"


@allure.title("Task - Test4 Mini Project Espo CRM")
@allure.description("TC4 - Verify user is able to click on Project Management link")
@pytest.mark.smoke
def test_proj_mgmt():
    chrome_options = Options()
    testdriver = webdriver.Chrome(chrome_options)
    testdriver.get("https://demo.us.espocrm.com/")
    testdriver.find_element(By.LINK_TEXT, "Project Management").click()
    print("TC4 passed")

    #assert testdriver.current_url == "https://www.espocrm.com/extensions/project-management/"


@allure.title("Task - Test5 Mini Project Espo CRM")
@allure.description("TC5 - Verify user is able to click on Personal Demo link")
@pytest.mark.smoke
def test_personal_demo():
    chrome_options = Options()
    testdriver = webdriver.Chrome(chrome_options)
    testdriver.get("https://demo.us.espocrm.com/")
    testdriver.find_element(By.LINK_TEXT, "personal demo").click()
    print("TC5 passed")

    #assert testdriver.current_url == "https://www.espocrm.com/cloud-registration/?plan=demo"

