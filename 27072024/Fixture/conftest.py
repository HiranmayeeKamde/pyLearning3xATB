import allure
import pytest
import requests


@pytest.fixture()
def create_token():
    print(" Creating Token!!")
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


@pytest.fixture()
def create_booking_id():
    print(" Creating Booking_id!!")
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


# Below function is in-build function
@pytest.fixture
def read_csv_file_data():
    pass


@pytest.fixture
def read_mysql_file_database():
    pass


@pytest.fixture
def launch_browser():
    print("Launching a Browser!! Chrome")
    return "chrome"


@pytest.fixture
def close_browser():
    print("Closing aBrowser !! Chrome")
    return "closed"


@pytest.fixture
def read_url_testdata_excel():
    pass
