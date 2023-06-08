from selenium.common.exceptions import TimeoutException

from support.helpers.drivers.wait import Wait


class Check:

    def __init__(self, wait: Wait):
        self.wait = wait

    def is_element_displayed(self, by_method_with_selector: tuple, timeout: int = 10) -> bool:
        try:
            self.wait.until_element_displayed(by_method_with_selector, timeout)
            return True
        except TimeoutException:
            return False

    def is_element_presented_on_page(self, by_method_with_selector: tuple, timeout: int = 10) -> bool:
        try:
            self.wait.until_element_presented_on_the_page(by_method_with_selector, timeout)
            return True
        except TimeoutException:
            return False

    def is_element_clickable(self, by_method_with_selector: tuple, timeout: int = 3) -> bool:
        try:
            self.wait.until_element_be_clickable(by_method_with_selector, timeout)
            return True
        except TimeoutException:
            return False

    def is_text_presented_in_element(self, by_method_with_selector: tuple, text: str, timeout: int = 10) -> bool:
        try:
            self.wait.until_text_to_be_presented_in_element(by_method_with_selector, text, timeout)
            return True
        except TimeoutException:
            return False

    def is_text_presented_in_element_value(self, by_method_with_selector, text, timeout: int = 10) -> bool:
        try:
            self.wait.until_text_to_be_presented_in_element_value(by_method_with_selector, text, timeout)
            return True
        except TimeoutException:
            return False
