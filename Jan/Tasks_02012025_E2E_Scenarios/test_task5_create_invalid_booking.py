# 5. Invalid Creation - enter a wrong payload or Wrong JSON.

import pytest
import allure
import requests

def test_create_invalid_booking():
    i_payload = {}
    i_url = "https://restful-booker.herokuapp.com/booking"
    i_headers = {
        "Content-Type" : "application/json"
    }

    result = requests.post(url=i_url,headers=i_headers,json=i_payload)
    #print(result.status_code)

    if (result.status_code !=200) :
        print("Invalid booking, please try again!")