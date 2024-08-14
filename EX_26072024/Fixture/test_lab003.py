import allure
import pytest
import requests


def test_update_req_1(create_token, create_booking_id):
    print("Token =", create_token)  # function use a variable when we mark as a fixture
    print("Booking id =", create_booking_id)

    base_url = "https://restful-booker.herokuapp.com"
    path_url = "/booking/" + str(create_booking_id)
    PUT_URL = base_url + path_url

    cookies = "token=" + create_token
    headers = {"Content-Type": "application/json",
               "Cookie": cookies
               }
    json_payload = {
        "firstname": "Hiranmayee",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.put(url=PUT_URL, headers=headers, json=json_payload)
    assert response.status_code == 200
    responseData = response.json()
    print(response.json())
    print(responseData["firstname"])
    assert responseData["firstname"] == "Hiranmayee"


def test_update_req_2(create_token, create_booking_id):
    print("Token =", create_token)  # function use a variable when we mark as a fixture
    print("Booking id =", create_booking_id)
    base_url = "https://restful-booker.herokuapp.com"
    path_url = "/booking/" + str(create_booking_id)
    PUT_URL = base_url + path_url

    cookies = "token=" + create_token
    headers = {"Content-Type": "application/json",
               "Cookie": cookies
               }
    json_payload = {
        "firstname": "Hiranmayee",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.put(url=PUT_URL, headers=headers, json=json_payload)
    assert response.status_code == 200
    responseData = response.json()
    print(response.json())
    print(responseData["firstname"])
    assert responseData["firstname"] == "Hiranmayee"
