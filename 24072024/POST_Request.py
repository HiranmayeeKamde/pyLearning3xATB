import allure
import pytest
import requests


@allure.title("TC1 Create booking CURD Positive")
@allure.description("TC1 - Verify the create Booking")
@pytest.mark.curd
def test_create_booking_positive_tc1():
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
    assert responseData["bookingid"] is not None
    assert responseData["bookingid"] > 0
    assert type(responseData["bookingid"]) == int
    firstname = responseData["booking"]["firstname"]
    assert firstname == "Jim"
    # checkin verification
    checkin = responseData["booking"]["bookingdates"]["checkin"]
    assert checkin == "2018-01-01"


@allure.title("TC2 Create booking CURD Negative")
@allure.description("TC2 - Verify Booking is not created with {} data")
@pytest.mark.curd
def test_create_booking_negative_tc2():
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
    payload = {}

    response = requests.post(url=URL, headers=headers, json=payload)  # (Positional Parameter)
    # Response body verification
    """
    Header 
    Status code
    JSON schema Validation
    Time response
    """
    print(type(URL))
    print(type(headers))
    print(type(payload))
    assert 500 == response.status_code

@allure.title("TC3 Create booking CURD Negative")
@allure.description("TC3 - Verify Booking with totalprice is string ")
@pytest.mark.curd
def test_create_booking_negative_tc3():
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
        "totalprice": "Hiranmayee",
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.post(url=URL, headers=headers, json=payload)  # (Positional Parameter)
    assert response.status_code == 200
    responseData = response.json()
    total_price = responseData["booking"]["totalprice"]
    assert total_price is None
    # Response body verification
    """
    Header 
    Status code
    JSON schema Validation
    Time response
    """
