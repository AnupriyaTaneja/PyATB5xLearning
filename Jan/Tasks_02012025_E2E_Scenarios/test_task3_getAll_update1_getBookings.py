# 3. Get an Existing Booking id from Get All Bookings Ids , Update a Booking and Verify using GET by id.

import pytest
import allure
import requests


def get_all_bookings(args):
    get_all_url = "https://restful-booker.herokuapp.com/booking"
    get_response = requests.get(get_all_url)
    if(args):
        url1 = get_all_url + "/" + str(args)
        response1 = requests.get(url1)
        print(response1.json())
    return get_response.json()


def create_token():
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
    # assert response_data.status_code == 200
    return token


def test_update_booking():
    booking_id = 1779
    auth = create_token()

    print("Bookings before update:")
    get_all_bookings(booking_id)

    # g_url = "https://restful-booker.herokuapp.com/booking/" + str(booking_id)
    # print(g_url)

    # print("Booking before update:")
    # get_all_bookings()
    # result_get = requests.get(url=g_url)
    # print(result_get.json())

    json_payload_update = {
        "firstname": "Test1",
        "lastname": "Test2",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    headers_test = {
        "Content-Type": "application/json",
        "Cookie": "token=" + auth
    }

    b_url = "https://restful-booker.herokuapp.com/booking/" + str(booking_id)

    result = requests.put(url=b_url, headers=headers_test, json=json_payload_update)
    print("---------")
    print("Booking after update:")
    print(result.json())
