import allure
import pytest


@allure.description("validate if calculator add option is working")
@allure.title("validate add function")
@allure.step("start validate title test")
@allure.severity(allure.severity_level.NORMAL)
@allure.epic("functionality")
@allure.feature("title - functionality")
@allure.story("validate add function")
@pytest.mark.flaky(reruns=1)
def test_android_wifi_connection_function(initialize):
    with allure.step("start test connect to WIFI network"):
        wifi_network_name = "Shlomi-mesh"
        wifi_password = "0585666667ABC"
        driver, wifi_settings_screen = initialize
        wifi_settings_screen.go_to_wifi_screen_settings()
        wifi_settings_screen.enable_wifi()
        wifi_settings_screen.load_wifi_networks()
        wifi_settings_screen.connect_to_wifi_network(WIFI_NETWORK_NAME)
        wifi_settings_screen.fill_password_on_network(WIFI_PASSWORD)
        wifi_settings_screen.click_connect_button()
        assert wifi_settings_screen.get_wifi_status(), "user was not connected to desired wifi network"
