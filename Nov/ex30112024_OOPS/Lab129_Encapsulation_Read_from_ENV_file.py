# Web Automation - Selenium
# Page - You are going automate
import os
from dotenv import load_dotenv

class VWOLoginPage:

    def __init__(self, email_arg, password_arg):
        self.email = email_arg
        self.password = password_arg

    def login_confirm(self):
        if self.email == "apt@gmail.com" and self.password == "Pass123":
            print("Allowed, Login Success")
        else:
            print("Login Failed")

load_dotenv()  # take environment variables from .env.

# Code of your application, which uses environment variables (e.g. from `os.environ` or
# `os.getenv`) as if they came from the actual environment.

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

print(email,password)

vwo_obj = VWOLoginPage(email, password)
vwo_obj.login_confirm()
