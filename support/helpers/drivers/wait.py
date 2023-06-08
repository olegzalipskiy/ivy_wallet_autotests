from typing import Callable, Any

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from support.helpers.logger import log
from support.utils.decorators import log_until


class Wait:
    def __init__(self, driver):
        self.driver = driver

    def _wait_until(self, ec: Callable, timeout: int):
        element = WebDriverWait(self.driver, timeout).until(ec)
        return element

    def _wait_until_not(self, ec: Callable, timeout: int):
        element = WebDriverWait(self.driver, timeout).until_not(ec)
        return element

    @log_until
    def until_element_displayed(self, method_with_selector: tuple, timeout: int) -> TimeoutException | Any:
        try:
            element = self._wait_until(EC.visibility_of_element_located(method_with_selector), timeout)
            return element
        except TimeoutException as e:
            _handle_exception(e, method_with_selector)

    @log_until
    def until_element_not_displayed(self, method_with_selector: tuple, timeout: int) -> WebElement:
        try:
            element = self._wait_until_not(EC.visibility_of_element_located(method_with_selector), timeout)
            return element
        except TimeoutException as e:
            _handle_exception(e, method_with_selector)

    @log_until
    def until_element_presented_on_the_page(self, method_with_selector: tuple, timeout: int) -> WebElement:
        try:
            element = self._wait_until(EC.presence_of_element_located(method_with_selector), timeout)
            return element
        except TimeoutException as e:
            _handle_exception(e, method_with_selector)

    @log_until
    def until_element_not_presented_on_the_page(self, method_with_selector: tuple, timeout: int) -> WebElement:
        try:
            element = self._wait_until_not(EC.presence_of_element_located(method_with_selector), timeout)
            return element
        except TimeoutException as e:
            _handle_exception(e, method_with_selector)

    @log_until
    def until_element_be_clickable(self, method_with_selector: tuple, timeout: int) -> WebElement:
        try:
            element = self._wait_until(EC.element_to_be_clickable(method_with_selector), timeout)
            return element
        except TimeoutException as e:
            _handle_exception(e, method_with_selector)

    @log_until
    def until_element_not_be_clickable(self, method_with_selector: tuple, timeout: int) -> WebElement:
        try:
            element = self._wait_until_not(EC.element_to_be_clickable(method_with_selector), timeout)
            return element
        except TimeoutException as e:
            _handle_exception(e, method_with_selector)

    @log_until
    def until_text_to_be_presented_in_element(self, method_with_selector: tuple, timeout: int, text: str) -> WebElement:
        try:
            element = self._wait_until(EC.text_to_be_present_in_element(method_with_selector, text), timeout)
            return element
        except TimeoutException as e:
            _handle_exception(e, method_with_selector)

    @log_until
    def until_text_to_be_not_presented_in_element(self, method_with_selector, text, timeout=10) -> WebElement:
        try:
            element = self._wait_until_not(EC.text_to_be_present_in_element(method_with_selector, text), timeout)
            return element
        except TimeoutException as e:
            _handle_exception(e, method_with_selector)

    @log_until
    def until_text_to_be_presented_in_element_value(self, method_with_selector: tuple,
                                                    timeout: int, text: str) -> WebElement:
        try:
            element = self._wait_until(EC.text_to_be_present_in_element_value(method_with_selector, text), timeout)
            return element
        except TimeoutException as e:
            _handle_exception(e, method_with_selector)

    @log_until
    def until_text_to_be_not_presented_in_element_value(self, method_with_selector: tuple, timeout: int, text: str):
        try:
            element = self._wait_until_not(EC.text_to_be_present_in_element_value(method_with_selector, text), timeout)
            return element
        except TimeoutException as e:
            _handle_exception(e, method_with_selector)


def _default_error_message(method_with_selector, e):
    strategy, locator = method_with_selector
    return f"""
    Element with locator 
    [ {locator} ]
    was not found by 
    [ {strategy} ] strategy.
    Error message: {e.args[0]}"""


def _handle_exception(exception: Exception, method_with_selector: tuple):
    msg = _default_error_message(method_with_selector, exception)
    log.error(msg)
    raise TimeoutException(msg)
