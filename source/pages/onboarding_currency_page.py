import json

import allure
from appium.webdriver.common.mobileby import MobileBy

from source.pages.base_page import BasePage
from support.helpers.mobile_locator import MobileLocator
from support.utils.file_system import FileSystem


class OnboardingCurrencyPage(BasePage):
    _TITLE = MobileLocator(
        android=(MobileBy.XPATH,
                 '//android.widget.TextView[@text="Choose currency"]')
    )

    _SUGGESTED_TITLE = MobileLocator(
        android=(MobileBy.XPATH,
                 '//android.widget.TextView[@text=Suggested]')
    )

    _CROSS_BUTTON = MobileLocator(
        android=(MobileBy.XPATH,
                 '(//android.widget.ImageView[@content-desc="icon button"])[1]')
    )

    _SEARCH_BUTTON = MobileLocator(
        android=(MobileBy.XPATH,
                 '(//android.widget.ImageView[@content-desc="icon button"])[2]')
    )

    _CHOOSE_BUTTON = MobileLocator(
        android=(MobileBy.XPATH,
                 '//android.view.View[@content-desc="icon"]/ancestor::android.view.View[4]')
    )

    _SEARCH_FIELD = MobileLocator(
        android=(MobileBy.XPATH,
                 '//android.widget.TextView[@text="Search (e.g. EUR, USD, BTC)"]/ancestor::android.widget.EditText')
    )

    _SEARCH_PLACEHOLDER = MobileLocator(
        android=(MobileBy.XPATH,
                 '//android.widget.TextView[@text="Search (e.g. EUR, USD, BTC)"]')
    )

    _SEARCH_ICON = MobileLocator(
        android=(MobileBy.XPATH,
                 '(//android.view.View[@content-desc="icon"])[1]')
    )

    _CANCEL_SEARCH_BUTTON = _SEARCH_BUTTON

    @staticmethod
    def generate_currency_locator(currency: str) -> MobileLocator:
        return MobileLocator(
            android=(MobileBy.XPATH,
                     f'//android.widget.TextView[@text="{currency}"]')
        )

    @allure.step("Title is displayed")
    def check_title_is_displayed(self):
        return self.driver.check.is_element_displayed(by_method_with_selector=self._TITLE())

    @allure.step("Suggested title is displayed")
    def check_suggested_title_is_displayed(self):
        return self.driver.check.is_element_displayed(by_method_with_selector=self._SUGGESTED_TITLE())

    @allure.step("Cross button is displayed")
    def check_cross_button_is_displayed(self):
        return self.driver.check.is_element_displayed(by_method_with_selector=self._CROSS_BUTTON())

    @allure.step("Search button is displayed")
    def check_search_button_is_displayed(self):
        return self.driver.check.is_element_displayed(by_method_with_selector=self._SEARCH_BUTTON())

    @allure.step("Choose button is displayed")
    def check_choose_button_is_displayed(self):
        return self.driver.check.is_element_displayed(by_method_with_selector=self._CHOOSE_BUTTON())

    @allure.step("Search field is displayed")
    def check_search_field_is_displayed(self):
        return self.driver.check.is_element_displayed(by_method_with_selector=self._SEARCH_FIELD())

    @allure.step("Search field placeholder is displayed")
    def check_search_field_placeholder_is_displayed(self):
        return self.driver.check.is_element_displayed(by_method_with_selector=self._SEARCH_PLACEHOLDER())

    @allure.step("Search icon is displayed")
    def check_search_icon_is_displayed(self):
        return self.driver.check.is_element_displayed(by_method_with_selector=self._SEARCH_ICON())

    @allure.step("Cancel search button is displayed")
    def check_cancel_search_button_is_displayed(self):
        return self.driver.check.is_element_displayed(by_method_with_selector=self._CANCEL_SEARCH_BUTTON())

    @allure.step("All suggested currency are displayed")
    def check_all_suggested_currency_are_displayed(self):
        currency_path = FileSystem.get_absolute_path("resourcers", "test_data", "suggested_currency_list.json")
        with open(currency_path) as currency_file:
            currency_list = json.load(currency_file)
        for currency in currency_list:
            return self.driver.check.is_element_displayed(
                by_method_with_selector=self.generate_currency_locator(currency))

    @allure.step("Tap on the 'Choose' button")
    def tap_in_choose_button(self):
        self.driver.click_on(self._CHOOSE_BUTTON())

    @allure.step("Tap on the 'Cross' button")
    def tap_in_cross_button(self):
        self.driver.click_on(self._CROSS_BUTTON())

    @allure.step("Tap on the 'Search' button")
    def tap_in_search_button(self):
        self.driver.click_on(self._SEARCH_BUTTON())

    @allure.step("Tap on the 'Cancel search' button")
    def tap_in_close_search(self):
        self.driver.click_on(self._CANCEL_SEARCH_BUTTON())

    @allure.step("Select one of the 'Suggested currency'")
    def tap_in_suggested_search(self, currency: str):
        currency_path = FileSystem.get_absolute_path("resourcers", "test_data", "suggested_currency_list.json")
        with open(currency_path) as currency_file:
            currency_list = json.load(currency_file)
        if currency in currency_list:
            self.driver.click_on(self.generate_currency_locator(currency)())
        else:
            raise Exception("Not correct currency")

    @allure.step("Execute search")
    def execute_search(self, input_text: str):
        self.driver.click_on(self._SEARCH_BUTTON())
        with allure.step(f'Fill field by value {input_text}'):
            self.driver.clear_field_and_fill(by_method_with_selector=self._SEARCH_FIELD(),
                                             input_value=input_text)
        with allure.step("Tap on 'Search' button"):
            self.driver.execute_script("mobile: performEditorAction", {"action": "search"})


class SelectedCurrencyElement(BasePage):

    @staticmethod
    def generate_selected_currency_locator(currency: str) -> MobileLocator:
        return MobileLocator(
            android=(MobileBy.XPATH,
                     f'//android.widget.TextView[@text="Selected"]/preceding-sibling::android.widget.TextView[@text="{currency}"]')
        )

    @allure.step("Check what selected currency is displayed")
    def check_selected_currency_is_displayed(self, currency: str):
        return self.driver.check.is_element_displayed(self.generate_selected_currency_locator(currency))
