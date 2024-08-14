"""
Scenario 1 : Verify that create Booking -> Patch Request -> Verify that firstname is updated
"""
import allure
import pytest
import requests


# Step 1 - Verify that create Booking
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

    # Step 2 - To Perform PATCH Request
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


# step 3 - Updating the firstname

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
    assert responseData["firstname"] == "Hiranmayee"
