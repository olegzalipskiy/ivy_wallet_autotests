from typing import Optional

from source.config import LANGUAGE, PLATFORM_NAME
from support.helpers.drivers.mobile_driver import MobileDriverWrapper


class PageObjectFactory:
    def __init__(self):
        self._mobile_driver: Optional[MobileDriverWrapper] = None
        self.language = LANGUAGE

    @property
    def mobile_driver(self) -> MobileDriverWrapper:
        if self._mobile_driver:
            return self._mobile_driver
        else:
            raise AttributeError('Mobile Driver is not initialized')

    @mobile_driver.setter
    def mobile_driver(self, mobile_driver: MobileDriverWrapper) -> None:
        self._mobile_driver = mobile_driver


POF = PageObjectFactory()
