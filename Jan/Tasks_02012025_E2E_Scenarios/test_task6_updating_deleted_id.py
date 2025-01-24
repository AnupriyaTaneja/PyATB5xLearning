# 6. Trying to Update on a Delete ID -> 404

import pytest
import allure
import requests


def test_create_token():
    test_url = "https://restful-booker.herokuapp.com/auth"
    test_header = {
        "Content-Type": "application/json"
    }
    test_json_payload = {
        "username": "admin",
        "password": "password123"
    }

    response_data = requests.post(url=test_url, headers=test_header, json=test_json_payload)
    response_json = response_data.json()
    token = response_json["token"]
    # print(token)
    assert response_data.status_code == 200
    return token


def test_create_booking():
    booking_url = "https://restful-booker.herokuapp.com/booking"

    booking_headers = {
        "Content-Type": "application/json"
    }

    booking_json = {
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

    booking_response = requests.post(url=booking_url, headers=booking_headers, json=booking_json)
    response_json = booking_response.json()
    booking_id = response_json["bookingid"]
    assert booking_response.status_code == 200
    print(response_json["booking"]["firstname"])
    print(booking_id)
    return booking_id


def test_delete_booking():

    auth_token = test_create_token()

    test_bookingid = test_create_booking()

    print(auth_token)
    print(test_bookingid)

    delete_url = "https://restful-booker.herokuapp.com/booking/" + str(test_bookingid)
    print(delete_url)

    delete_headers = {
        "Content-Type": "application/json",
        "Cookie": "token=" + auth_token
    }

    res = requests.patch(url=delete_url, headers=delete_headers)
    print(res)
    res_json = res.json()
    print("Record successfully deleted for booking id:", test_bookingid)
    assert res.status_code == 200
    return test_bookingid


def test_update_deleted_booking():
    my_token = test_create_token()
    b_id = test_delete_booking()

    update_url = "https://restful-booker.herokuapp.com/booking/" + str(b_id)

    header_test = {
        "Content-Type" : "application/json",
        "Cookie" : "token=" + my_token
    }

    payload = {
    "firstname" : "Jill",
    "lastname" : "Bobbi",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}

    response_put = requests.put(url=update_url,headers=header_test,json=payload)
    print(response_put)
    if response_put.status_code == 200 :
        print("Booking id ", b_id, "does not exist")

