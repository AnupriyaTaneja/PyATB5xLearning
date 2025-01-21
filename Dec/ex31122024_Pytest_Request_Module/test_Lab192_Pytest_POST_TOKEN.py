import pytest
import allure
import requests

base_url = "https://restful-booker.herokuapp.com"  # global variable
var_header = {"Content-Type": "application/json"}


# Create Token - POST
def test_create_token():


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
