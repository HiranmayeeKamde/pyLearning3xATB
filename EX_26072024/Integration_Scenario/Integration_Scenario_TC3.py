"""
Scenario 3 : Get existing id from Get All booking IDs, update Booking and verify using GET by id
"""
"""
Step 1 : Get all existing Booking by IDs
Step 2 : Update Booking
Step 3 : Verify using GET by id
"""
import allure
import pytest
import requests


# Step 1 : Get all existing Booking by IDs

def test_get_all_booking_ids():
    url = "https://restful-booker.herokuapp.com/booking"
    responseData = requests.get(url)
    print(responseData.json())
    booking_id = responseData
    assert responseData.status_code == 200

    # Step 2 : Update Booking
    """
        1. URL
        2. Path -> Booking_id
        3. Token - Auth 
        4. Payload
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


# Step 2 : Update Booking
"""
1. URL
2. Booking Id
3. Cookies = > token
4. Header
5. Payload
6. Request
7. Response
8. verification updated patch
"""


@allure.title("TC#2 : Updating the firstname ")
@allure.title("Step 3 - Verify that firstname is updated")
@pytest.mark.ist
def test_updating_firstname_tc2():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(create_booking())
    PUT_URL = base_url + base_path
    cookies = "token=" + create_token()
    header = {"Content-Type": "application/json",
              "cookie": cookies}
    payload = {
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
    response = requests.put(url=PUT_URL, headers=header, json=payload)
    assert response.status_code == 200
    responseData = response.json()

    # verify the firstname is updated
    print(responseData["firstname"])
    print(responseData["bookingid"])
    booking_id = responseData["bookingid"]
    assert booking_id == str(create_booking())
