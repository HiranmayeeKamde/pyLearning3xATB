# to perform PUT Request
"""
1. URL
2. Path -Bookingid
3. Token - Auth
4. Payload
"""


import allure
import pytest
import requests


# Creating a token
def create_token():
    # URL
    URL = "https://restful-booker.herokuapp.com/auth"
    # Header
    headers = {"Content-Type": "application/json"}
    # Body
    payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=URL, headers=headers, json=payload)
    token = response.json()["token"]
    print(token)
    return token


# Creating a Booking_id
def create_booking():
    # To make request
    # URL = "https://restful-booker.herokuapp.com/booking"
    # Method = POST
    # Header = {"Content-Type" : "application/json"}
    # Payload = Dictionary --> (body)
    # Auth = (verify the user identity)

    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    # URL
    URL = base_url + base_path
    # Headers
    headers = {"Content-Type": "application/json"}
    # Payload
    payload = {
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

    response = requests.post(url=URL, headers=headers, json=payload)  # (Positional Parameter)
    assert response.status_code == 200
    # Response body verification
    """
    Header 
    Status code
    JSON schema Validation
    Time response
    """
    responseData = response.json()
    booking_id = responseData["bookingid"]
    return booking_id


# Update_booking_id = token +create_booking_id
@allure.testcase("TC#1")
def test_update_booking_id_tc1():
    base_url = "https://restful-booker.herokuapp.com"
    path_url = "/booking/" + str(create_booking())
    PUT_URL = base_url + path_url

    cookies = "token=" + create_token()
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

# Can i delete after creation

def test_delete():
    url= "https://restful-booker.herokuapp.com/booking"
    booking_id = create_booking()
    DELETE_url = url + str(booking_id)
    cookies = "token=" + create_token()
    headers = {"Content-Type": "application/json",
               "Cookie": cookies
               }
    print(headers)
    response = requests.delete(url=DELETE_url, headers=headers)