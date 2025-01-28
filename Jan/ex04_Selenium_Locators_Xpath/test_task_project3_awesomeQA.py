# Automation for the Registration Page of the AwesomeQA.com/UI
# Open - https://awesomeqa.com/ui/index.php?route=account/register
# Fill the form
# Verify that next page give - Your Account Has Been Created!
import os

import allure
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

def test_registration():
    load_dotenv()
    my_driver = webdriver.Chrome()
    my_driver.get("https://awesomeqa.com/ui/index.php?route=account/register")
    time.sleep(2)

    #<input type="text" name="firstname" value="" placeholder="First Name"
    # id="input-firstname" class="form-control" fdprocessedid="ulx6k">

    fname= my_driver.find_element(By.CSS_SELECTOR, "input[id='input-firstname']")
    fname.send_keys(os.getenv("MINI_PROJECT_FNAME"))
    time.sleep(1)

    #<input type="text" name="lastname" value="" placeholder="Last Name" id="input-lastname"
    # class="form-control" fdprocessedid="argxha">

    lname = my_driver.find_element(By.CSS_SELECTOR, "input[id='input-lastname']")
    lname.send_keys(os.getenv("MINI_PROJECT_LNAME"))
    time.sleep(1)

    #<input type="email" name="email" value="" placeholder="E-Mail" id="input-email"
    # class="form-control" fdprocessedid="ii5rj">
    myEmail = my_driver.find_element(By.CSS_SELECTOR, "input[id='input-email']")
    myEmail.send_keys(os.getenv("MINI_PROJECT_EMAIL"))
    time.sleep(1)

    #<input type="tel" name="telephone" value="" placeholder="Telephone" id="input-telephone"
    # class="form-control" fdprocessedid="pz81gp">
    myPhone = my_driver.find_element(By.CSS_SELECTOR, "input[id='input-telephone']")
    myPhone.send_keys(os.getenv("MINI_PROJECT_TEL"))
    time.sleep(1)

    #<input type="password" name="password" value="" placeholder="Password" id="input-password"
    # class="form-control" fdprocessedid="a3mqq5">
    myPass = my_driver.find_element(By.CSS_SELECTOR, "input[id='input-password']")
    myPass.send_keys(os.getenv("MINI_PROJECT_PASS"))
    time.sleep(1)

    # <input type="password" name="confirm" value="" placeholder="Password Confirm" id="input-confirm"
    # class="form-control" fdprocessedid="1vde9k">
    cPass = my_driver.find_element(By.CSS_SELECTOR, "input[id='input-confirm']")
    cPass.send_keys(os.getenv("MINI_PROJECT_CONFIRM_PASS"))
    time.sleep(1)

    # <label class="radio-inline">
    #                 <input type="radio" name="newsletter" value="1">
    #                 Yes</label>

    news_letter =my_driver.find_element(By.XPATH, "//input[@type = 'radio' and @name='newsletter']")
    news_letter.send_keys('Yes')
    news_letter.click()
    time.sleep(1)

    # <div class="pull-right">I have read and agree to the <a href="https://awesomeqa.com/ui/index.php?route=information/information/agree&amp;information_id=3" class="agree"><b>Privacy Policy</b></a>
    #                         <input type="checkbox" name="agree" value="1">
    #                         &nbsp;
    #             <input type="submit" value="Continue" class="btn btn-primary" fdprocessedid="5uha7">
    #           </div>

    privacy_policy = my_driver.find_element(By.XPATH, "//input[@type = 'checkbox' and @name='agree']" )
    privacy_policy.click()
    time.sleep(1)
#<input type="submit" value="Continue" class="btn btn-primary" fdprocessedid="5uha7">
    cont_button = my_driver.find_element(By.XPATH, "//input[@type = 'submit' and @value = 'Continue' and @class='btn btn-primary']")
    cont_button.click()
    time.sleep(2)

     # <div id="content" class="col-sm-9">
    #       <h1>Your Account Has Been Created!</h1>
    #       <p>Congratulations! Your new account has been successfully created!</p>
    #       <p>You can now take advantage of member privileges to enhance your online shopping experience with us.</p>
    #       <p>If you have ANY questions about the operation of this online shop, please e-mail the store owner.</p>
    #       <p>A confirmation has been sent to the provided e-mail address. If you have not received it within the hour, please
    #       <a href="https://awesomeqa.com/ui/index.php?route=information/contact">contact us</a>.</p>
    #       <div class="buttons">
    #         <div class="pull-right"><a href="https://awesomeqa.com/ui/index.php?route=account/account" class="btn btn-primary">Continue</a></div>
    #       </div>
    #       </div>
    confirm_msg = my_driver.find_element(By.CLASS_NAME, "col-sm-9")
    print(confirm_msg.text)
    time.sleep(3)

    my_driver.quit()

