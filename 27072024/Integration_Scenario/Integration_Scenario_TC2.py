"""
Scenario 2 : Create booking, Delete the booking with ID and verify using ID and verify using GET request
             that it should not exist.
"""

"""
Step 1- Create Booking ID
Step 2 - Delete Booking by id
Step 3 - verify deleted booking id
Step 4= Verify using GET Request that it should not exists
"""

import allure
import pytest
import requests


# Step 1- Create Booking ID
@allure.title("TC#1 : Crete Booking Positive ")
@allure.title("Step 1 - Verify that create Booking")
@pytest.mark.ist
def test_crete_booking_positive_tc1():
    """
    To make REQUEST:
    1. URL
    2. Method -> POST
    3. Header -> {"Content-Type": "application/json"}
    4. Payload -> Dictionary(Body)
    5. Auth -X
    """
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    header = {"Content-Type": "application/json"}
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

    response = requests.post(url=URL, headers=header, json=payload)

    # Verification of response body
    assert response.status_code == 200
    responseData = response.json()  # Concerted to JSON
    assert responseData["bookingid"] is not None

    # Step 2 - Delete Booking by id
    """
    1. URL
    2. Booking_id
    3. Token
    4. header
    5. Request
    6. Response
    """


# ----- 1. Creating a Token ---------
def create_token():
    """
    1. URL
    2. Header
    3. Body
    4. Request
    5. Response
    6. Token
    """
    URL = "https://restful-booker.herokuapp.com/auth"
    header = {"Content-Type": "application/json"}
    payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=URL, headers=header, json=payload)
    token = response.json()["token"]
    print(token)
    return token


# ----- 2. Creating a Booking ---------
def create_booking():
    """
        To make REQUEST:
        1. URL
        2. Method -> POST
        3. Header -> {"Content-Type": "application/json"}
        4. Payload -> Dictionary(Body)
        5. Auth -X
        """
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    header = {"Content-Type": "application/json"}
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

    response = requests.post(url=URL, headers=header, json=payload)

    # Verification of response body
    assert response.status_code == 200
    responseData = response.json()  # Concerted to JSON
    booking_id = responseData["bookingid"]
    return booking_id


# ----------3. I can DELETE after creating Booking------------------------
@allure.title("TC#2 : Deleting Booking  ")
@allure.title("Step 1 - Verify that Booking is deleted ")
@pytest.mark.ist
def test_delete_booking_tc2():
    url = "https://restful-booker.herokuapp.com/booking/"
    booking_id = create_booking()
    DELETE_url = url + str(booking_id)
    cookies = "token=" + create_token()
    header = {"Content-Type": "application/json",
              "cookie": cookies}
    print(header)
    response = requests.delete(url=DELETE_url, headers=header)
    assert response.status_code == 201   # created- > deleted by id
    # Verifying deleted booking id should not be exists
    responseData = requests.get(DELETE_url)
    assert responseData.status_code == 404  # 404 = Not Found
