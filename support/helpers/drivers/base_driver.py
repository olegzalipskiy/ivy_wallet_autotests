from abc import ABC, abstractmethod

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver

from support.helpers.drivers.check import Check
from support.helpers.drivers.wait import Wait
from support.helpers.logger import log

from support.utils.decorators import handle_stale_element_exception

class BaseDriverWrapper(ABC):
    def __init__(self):
        driver = self._get_driver()
        self.driver = EventFiringWebDriver(driver, CustomListener())
        self.wait = Wait(self.driver.wrapped_driver)
        self.check = Check(self.wait)

    @abstractmethod
    def _get_driver(self) -> str:
        raise NotImplementedError

    def close_driver(self) -> None:
        """Closes driver"""
        self.driver.quit()

    def get_element(self, by_method_with_selector: tuple, timeout: int = 10) -> WebElement:
        """
        Method encapsulates finding one element on the page
        :param by_method_with_selector: a tuple which contains 2 elements:
            1. By.method, which can be got from selenium.webdriver.common.by import By
            2. Selector according to selected method
        :param timeout: optional parameter which can specify how long method will try to find element
        :return: Web element which would be found according to selector,
            if nothing would be found an exception will be raised
        """
        return self.wait.until_element_presented_on_the_page(by_method_with_selector, timeout)

    def get_elements(self, by_method_with_selector: tuple) -> list[WebElement]:
        """
        Method encapsulates finding many element on the page
        :param by_method_with_selector: a tuple which contains 2 elements:
            1. By.method, which can be got from selenium.webdriver.common.by import By
            2. Selector according to selected method
        :return: list of web elements, if nothing would be found - empty list will be returned
        """
        return self.driver.find_elements(*by_method_with_selector)

    def get_displayed_element(self, by_method_with_selector: tuple, timeout: int = 10) -> WebElement:
        return self.wait.until_element_displayed(by_method_with_selector, timeout)

    def get_element_text(self, by_method_with_selector: tuple, timeout: int = 10) -> str:
        return self.get_displayed_element(by_method_with_selector, timeout).text

    def get_elements_text(self, by_method_with_selector: tuple) -> list[str]:
        elements = self.get_elements(by_method_with_selector)
        return [element.text for element in elements]

    def get_element_attribute(self, by_method_with_selector: tuple, attribute_name: str, timeout: int = 10) -> str:
        return self.get_element(by_method_with_selector, timeout).get_attribute(attribute_name)

    @handle_stale_element_exception
    def click_on(self, by_method_with_selector: tuple, timeout: int = 10) -> None:
        self.wait.until_element_be_clickable(by_method_with_selector, timeout).click()

    @handle_stale_element_exception
    def clear_field_and_fill(self, by_method_with_selector: tuple, input_value: str, timeout: int = 10) -> None:
        element = self.wait.until_element_be_clickable(by_method_with_selector, timeout)
        element.click()
        element.clear()
        element.send_keys(input_value)


class CustomListener(AbstractEventListener):

    def on_exception(self, exception, driver):
        log.critical(f" - Exception [ {exception} ] - ")

    def before_find(self, by, value, driver):
        log.debug(f"Trying to find [ {value} ] by method [ {by} ]")

    def after_find(self, by, value, driver):
        log.debug(f"Found [ {value} ] by method [ {by} ] ")

    def before_click(self, element, driver):
        log.debug(f"Trying to click [ {element} ] element")

    def after_click(self, element, driver):
        log.debug(f"Clicked on the [ {element} ] the element")

    def before_execute_script(self, script, driver):
        log.debug(f"Executing script [ {script} ]")

    def before_close(self, driver):
        log.warning(f" - Closing current tab - ")

    def before_quit(self, driver):
        log.warning(f"Quiting drivers")

    def after_quit(self, driver):
        log.warning(f"Quit drivers")
