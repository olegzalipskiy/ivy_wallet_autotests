from support.helpers.drivers.mobile_driver import MobileDriverWrapper


class BasePage:
    def __init__(self, driver: MobileDriverWrapper):
        self.driver = driver
