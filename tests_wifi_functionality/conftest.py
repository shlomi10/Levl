import allure
import pytest
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions

from tests_wifi_functionality.Constants import APPIUM_HOST
from pages.WifiSettingsScreen import WifiSettingsScreen


@pytest.fixture(scope="session", autouse=True)
def initialize():
    cap: Dict[str, Any] = {
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "platformVersion": "14",
        "deviceName": "Android",
        "noReset": True
    }
    global driver
    driver = webdriver.Remote(APPIUM_HOST, options=AppiumOptions().load_capabilities(cap))
    calculator_main = WifiSettingsScreen(driver)
    yield driver, calculator_main
    driver.quit()


def pytest_exception_interact(report):
    if report.failed:
        allure.attach(body=driver.get_screenshot_as_png(), name="screenshot",
                      attachment_type=allure.attachment_type.PNG)
