import allure
import pytest
import requests

# launch_browser and close_browser coming from conftext.py file
def test_selenium(launch_browser, close_browser):
    launch_browser
    print("do Something!")
    close_browser
