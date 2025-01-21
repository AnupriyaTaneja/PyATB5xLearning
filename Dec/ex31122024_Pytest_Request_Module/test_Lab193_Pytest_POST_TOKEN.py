from http.client import responses

import pytest
import allure
import requests

base_url = "https://restful-booker.herokuapp.com"  # global variable
var_header = {"Content-Type": "application/json"}


# Create Token - POST
def get_token():

    base_path_token = "/auth"
    full_url = base_url + base_path_token
    json_payload_auth = {
        "username": "admin",
        "password": "password123"
    }
    response_auth = requests.post(url=full_url, headers=var_header, json=json_payload_auth)
    print("Response code:" , response_auth)

    assert response_auth.status_code == 200

    response_auth_json = response_auth.json()
    auth_token = response_auth_json["token"]

    print("Authorization token:" , auth_token)

    assert type(auth_token) == str
    assert len(auth_token) > 0

    return auth_token

def get_booking_id():
    base_path_getbooking = "/booking"
    full_url = base_url + base_path_getbooking
    print(full_url)

    json_payload = {
            "firstname": "Jim",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }

    booking_response = requests.post(url=full_url,headers=var_header,json=json_payload)

    booking_response_json = booking_response.json()
    b_id = booking_response_json["bookingid"]
    return b_id

def test_put_request():
    access_token = get_token()
    booking_id = get_booking_id()
    print(access_token)
    print(booking_id)

    base_path_put = "/booking/" + str(booking_id)
    full_url_put = base_url + base_path_put
    print(full_url_put)

    auth_cookie = "token=" + access_token
    print(auth_cookie)

    json_paylod_update = {
        "firstname": "James",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    update_header = {
        "Content-Type" : "application/json",
        "Cookie" : auth_cookie
    }

    put_response = requests.put(url=full_url_put,headers=update_header,json=json_paylod_update)
    print(put_response)

    assert put_response.status_code == 200
    assert put_response.json()["firstname"] == "James"



