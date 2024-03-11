from appium.webdriver.common.appiumby import AppiumBy
from pages.BasePage import BasePage


class WifiSettingsScreen(BasePage):

    progressBar = (AppiumBy.ID, 'com.android.settings:id/progress_bar_animation')
    wifi_names = (AppiumBy.ID, 'android:id/title')
    password_field = (AppiumBy.ID, 'com.android.settings:id/password')
    connect_button = (AppiumBy.ID, 'android:id/button1')
    settings_button_when_connected = (AppiumBy.ID, 'com.android.settings:id/settings_button_no_background')

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_wifi_screen_settings(self):
        self.go_to_wifi_screen()

    def enable_wifi(self):
        self.enable_wifi_settings()

    def load_wifi_networks(self):
        self.wait_some_time(4)

    def connect_to_wifi_network(self, text_to_search):
        self.click_on_element_from_list(self.wifi_names, text_to_search)

    def fill_password_on_network(self, pwd):
        self.wait_some_time(4)
        self.fill_text(self.password_field, pwd)

    def wait_for_connect_button(self):
        self.wait_for_element_to_be_clickable(self.connect_button)

    def click_connect_button(self):
        self.click_on_element(self.connect_button)

    def get_wifi_status(self) -> bool:
        return self.wait_for_element_to_be_clickable(self.settings_button_when_connected)
