import time

import allure
from selenium.webdriver import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import subprocess


class BasePage(object):

    def __init__(self, driver):
        self.driver: WebDriver = driver

    wifi_settings = "adb shell am start -a android.settings.WIFI_SETTINGS"
    adb_command = "adb start-server"
    adb_start_wifi = "adb shell svc wifi enable"

    @allure.step("start ADB")
    def start_adb(self) -> None:
        try:
            subprocess.run(self.adb_command, shell=True, check=True)
            print("ADB started successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error starting ADB: {e}")

    @allure.step("go to WIFI screen")
    def go_to_wifi_screen(self) -> None:
        try:
            result = subprocess.run(self.wifi_settings, shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                print("Command executed successfully. \n you are at WIFI settings")
                print("Output:", result.stdout)
            else:
                print("Error executing command. \n you are not at WIFI settings")
                print("Error:", result.stderr)
        except Exception as e:
            print("An error occurred:", e)

    @allure.step("enable WIFI")
    def enable_wifi_settings(self) -> None:
        try:
            subprocess.run(self.adb_start_wifi, shell=True, check=True)
            print("WIFI started successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error starting WIFI: {e}")

    @allure.step("wait")
    def wait_some_time(self, timeout) -> bool:
        try:
            time.sleep(timeout)
            return True
        except TimeoutException:
            print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME!")
            self.driver.quit()
            return False

    @allure.step("click on element locator from list")
    def click_on_element_from_list(self, locator, text_to_search) -> bool:
        try:
            item_list = self.driver.find_elements(*locator)
            for item in item_list:
                if item.text == text_to_search:
                    item.click()
                    return True
        except Exception as e:
            print(f"Error click on element from list: {e}")
            allure.attach(body=self.driver.find_element(*locator).click(), name="click on element from list",
                          attachment_type=allure.attachment_type.TEXT)
            return False

    @allure.step("click on element locator")
    def click_on_element(self, locator) -> bool:
        try:
            self.driver.find_element(*locator).click()
            return True
        except Exception as e:
            print(f"Error click on element: {e}")
            allure.attach(body=self.driver.find_element(*locator).click(), name="click on element",
                          attachment_type=allure.attachment_type.TEXT)
            return False

    @allure.step("fill text on locator")
    def fill_text(self, locator, txt: str) -> bool:
        try:
            elem = self.driver.find_element(*locator)
            elem.clear()
            elem.send_keys(txt)
            return True
        except Exception as e:
            print(f"Error fill text on locator: {e}")
            allure.attach(body=self.driver.find_element(*locator).send_keys(txt), name="fill text on locator",
                          attachment_type=allure.attachment_type.TEXT)
            return False

    @allure.step("wait for element locator to be clickable")
    def wait_for_element_to_be_clickable(self, locator) -> bool:
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
            return True
        except TimeoutException:
            allure.attach(body=self.driver.find_element(*locator).send_keys(Keys.RETURN), name="wait for element to "
                                                                                               "be clickable",
                          attachment_type=allure.attachment_type.TEXT)
            print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" % (locator[1]))
            self.driver.quit()
            return False
