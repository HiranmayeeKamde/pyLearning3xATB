import pytest  # pip install pytest
import allure  # pip install allure-pytest
import requests # pip install requests


@allure.title("Teat GET REQUEST -Restfull Booker Project#1")
@allure.description("TC#1-> Verify the GET Request with ID works")
@allure.tag("regression", "p0", "smoke")
@allure.label("owner", "HiranmayeeKamde")
@allure.testcase("TC#1")
@pytest.mark.smoke
def test_get_single_request_by_id():
    url = "https://restful-booker.herokuapp.com/booking/2"
    responseData = requests.get(url)
    print(responseData.text)
    print(responseData.cookies)
    print(responseData.headers)
    print(responseData.text)
    print(responseData.json())
    assert 200 == responseData.status_code


@allure.title("Teat GET REQUEST -Restfull Booker Project#1")
@allure.description("TC#2-> Verify the GET Request with invalid booking ID")
@pytest.mark.smoke
def test_get_single_request_by_id_negative():
    url = "https://restful-booker.herokuapp.com/booking/invalid"
    responseData = requests.get(url)
    assert 404 == responseData.status_code


@allure.title("Teat GET REQUEST -Restfull Booker Project#1")
@allure.description("TC#3-> Verify the GET Request with same booking ID")
@pytest.mark.smoke
def test_get_single_request_by_id_negative2():
    url = "https://restful-booker.herokuapp.com/booking/2"
    responseData = requests.get(url)
    assert responseData.status_code == 404


@allure.title("Teat GET REQUEST -Restfull Booker Project#1")
@allure.description("TC#4-> Verify the GET Request with ID works")
@allure.testcase("TC#4")
def test_get_single_request_by_id_TC4():
    url = "https://restful-booker.herokuapp.com/booking/2"
    responseData = requests.get(url)
    print(responseData.text)
    print(responseData.cookies)
    print(responseData.headers)
    print(responseData.text)
    print(responseData.json())
    assert 200 == responseData.status_code