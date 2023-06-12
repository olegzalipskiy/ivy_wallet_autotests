from source.tests.base_test import BaseUITest
from support.helpers.page_object_factory import POF
from support.utils.verify import Verify


class TestOnboardingCurrencyPage(BaseUITest):

    def test_title_is_displayed(self):
        onboarding_currency_page = POF.get_onboarding_currency_page()
        Verify.is_true(actual_result=onboarding_currency_page.check_title_is_displayed,
                       verify_message="Title is not displayed")

    def test_suggested_title_is_displayed(self):
        onboarding_currency_page = POF.get_onboarding_currency_page()
        Verify.is_true(actual_result=onboarding_currency_page.check_suggested_title_is_displayed,
                       verify_message="Suggested currency title is not displayed")

    def test_cross_button_is_displayed(self):
        onboarding_currency_page = POF.get_onboarding_currency_page()
        Verify.is_true(actual_result=onboarding_currency_page.check_cross_button_is_displayed,
                       verify_message="Cross button is not displayed")

    def test_search_button_is_displayed(self):
        onboarding_currency_page = POF.get_onboarding_currency_page()
        Verify.is_true(actual_result=onboarding_currency_page.check_search_button_is_displayed,
                       verify_message="Search button is displayed")

    def test_choose_button_is_displayed(self):
        onboarding_currency_page = POF.get_onboarding_currency_page()
        Verify.is_true(actual_result=onboarding_currency_page.check_choose_button_is_displayed,
                       verify_message="Choose button is not displayed")

    def test_search_button_is_displayed(self):
        onboarding_currency_page = POF.get_onboarding_currency_page()
        Verify.is_true(actual_result=onboarding_currency_page.check_search_button_is_displayed,
                       verify_message="Search button is not displayed")

    def test_all_suggested_currency_is_displayed(self):
        onboarding_currency_page = POF.get_onboarding_currency_page()
        Verify.is_true(actual_result=onboarding_currency_page.check_all_suggested_currency_are_displayed,
                       verify_message="One of element in suggested currency is not displayed")

    def test_user_can_click_in_search_button(self):
        onboarding_currency_page = POF.get_onboarding_currency_page()
        Verify.is_true(actual_result=onboarding_currency_page.check_search_button_is_displayed,
                       verify_message="Search button is not displayed")
        onboarding_currency_page.tap_in_search_button()
        Verify.is_true(actual_result=onboarding_currency_page.check_search_field_is_displayed,
                       verify_message="Search field is not displayed")
        Verify.is_true(actual_result=onboarding_currency_page.check_search_field_placeholder_is_displayed,
                       verify_message="Placeholder in search field is not displayed")
        Verify.is_true(actual_result=onboarding_currency_page.check_search_icon_is_displayed,
                       verify_message="Search icon is not displayed")
        Verify.is_true(actual_result=onboarding_currency_page.check_cancel_search_button_is_displayed,
                       verify_message="Cancel search button is not displayed")

    def test_search_field_is_displayed(self):
        onboarding_currency_page = POF.get_onboarding_currency_page()
        Verify.is_true(actual_result=onboarding_currency_page.check_search_button_is_displayed,
                       verify_message="Search button is not displayed")
        onboarding_currency_page.tap_in_search_button()
        Verify.is_true(actual_result=onboarding_currency_page.check_search_field_is_displayed,
                       verify_message="Search field is not displayed")

    def test_placeholder_in_search_field_is_displayed(self):
        onboarding_currency_page = POF.get_onboarding_currency_page()
        Verify.is_true(actual_result=onboarding_currency_page.check_search_button_is_displayed,
                       verify_message="Search button is not displayed")
        onboarding_currency_page.tap_in_search_button()
        Verify.is_true(actual_result=onboarding_currency_page.check_search_field_placeholder_is_displayed,
                       verify_message="Placeholder in search field is not displayed")

    def test_search_icon_is_displayed(self):
        onboarding_currency_page = POF.get_onboarding_currency_page()
        Verify.is_true(actual_result=onboarding_currency_page.check_search_button_is_displayed,
                       verify_message="Search button is not displayed")
        onboarding_currency_page.tap_in_search_button()
        Verify.is_true(actual_result=onboarding_currency_page.check_search_icon_is_displayed,
                       verify_message="Search icon is not displayed")

    def test_cancel_search_icon_is_displayed(self):
        onboarding_currency_page = POF.get_onboarding_currency_page()
        Verify.is_true(actual_result=onboarding_currency_page.check_search_button_is_displayed,
                       verify_message="Search button is not displayed")
        onboarding_currency_page.tap_in_search_button()
        Verify.is_true(actual_result=onboarding_currency_page.check_cancel_search_button_is_displayed,
                       verify_message="Cancel search button is not displayed")

    def test_tap_in_suggested_currency_element(self):
        currency = "USD"
        onboarding_currency_page = POF.get_onboarding_currency_page()
        onboarding_currency_page.tap_in_suggested_search(currency=currency)
        # TODO: Add check after adding confirmation page

    def test_execute_search(self):
        currency = "USD"
        onboarding_currency_page = POF.get_onboarding_currency_page()
        onboarding_currency_page.tap_in_search_button
        onboarding_currency_page.execute_search(input_text=currency)
        list_of_search_results = onboarding_currency_page.get_search_results(currency)
        list_of_check_results = []
        for _ in list_of_search_results:
            list_of_check_results.append(currency in _)

        Verify.is_true(actual_result=all(list_of_check_results),
                       verify_message="Not correct search results")

    def test_select_currency_from_search_results(self):
        currency = "USD"
        onboarding_currency_page = POF.get_onboarding_currency_page()
        onboarding_currency_page.tap_in_search_button
        onboarding_currency_page.execute_search(input_text=currency)
        onboarding_currency_page.tap_currency_from_list(currency)
        # TODO: Add check after adding confirmation page
