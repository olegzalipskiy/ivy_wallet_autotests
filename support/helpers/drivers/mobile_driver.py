from appium import webdriver

from source.config import ENVIRONMENT_URL, OS

from support.helpers.drivers.base_driver import BaseDriverWrapper
from support.helpers.logger import log


class MobileDriverWrapper(BaseDriverWrapper):
    def __init__(self, desired_capabilities: dict):
        self.desired_capabilities = desired_capabilities
        super().__init__()
        log.info('Mobile driver initialized')

    def _get_driver(self):
        self.platform = OS
        return webdriver.Remote(ENVIRONMENT_URL, self.desired_capabilities)

    def swipe(self, direction, duration=800) -> None:
        """
        This method scrolls in all directions from the center of the screen.
        Direction means direction in which screen will move.
        Right direction it's a swipe from the right to the left, screen moves to the right.
        Duration of swipe as a default is 800 ms - it allows swipe slowly, so that swipe less than screen height
        """
        screen_width = self.driver.get_window_size().get('width')
        screen_height = self.driver.get_window_size().get('height')

        scroll_directions = {
            "down": {
                "start_x": int(0.5 * screen_width),
                "start_y": int(0.5 * screen_height),
                "end_x": int(0.5 * screen_width),
                "end_y": int(0.3 * screen_height),
            },
            "small swipe down":  {
                "start_x": int(0.5 * screen_width),
                "start_y": int(0.7 * screen_height),
                "end_x": int(0.5 * screen_width),
                "end_y": int(0.6 * screen_height)
            },
            "up": {
                "start_x": int(0.5 * screen_width),
                "start_y": int(0.3 * screen_height),
                "end_x": int(0.5 * screen_width),
                "end_y": int(0.7 * screen_height),
            },
            "left": {
                "start_x": int(0.2 * screen_width),
                "start_y": int(0.5 * screen_height),
                "end_x": int(0.8 * screen_width),
                "end_y": int(0.5 * screen_height),
            },
            "right": {
                "start_x": int(0.8 * screen_width),
                "start_y": int(0.5 * screen_height),
                "end_x": int(0.2 * screen_width),
                "end_y": int(0.5 * screen_height),
            }
        }
        start_x, start_y = scroll_directions[direction]['start_x'], scroll_directions[direction]['start_y']
        end_x, end_y = scroll_directions[direction]['end_x'], scroll_directions[direction]['end_y']

        log.info(f'Swipe {direction}. Start X: {start_x}. Start Y: {start_y}. End X: {end_x}. End Y: {end_y}.')
        self.driver.swipe(start_x=start_x, start_y=start_y, end_x=end_x, end_y=end_y, duration=duration)

    def swipe_until_element_displayed(self, element_locator, timeout=0, direction='down',
                                      retries_count=5, duration=800) -> None:
        log.debug(f'Start swiping {direction} until element will be displayed - {element_locator}')
        found_status = 'NOT FOUND'
        for try_ in range(retries_count):
            if self.check.is_element_displayed(element_locator, timeout):
                found_status = 'FOUND'
                log.debug(f'Finish swiping. Element is found on {try_ + 1} swipe; Element - {found_status}')
                break
            else:
                self.swipe(direction=direction, duration=duration)
        else:
            log.debug(f'Finish swiping. Element is not found after {retries_count} swipes; Element - {found_status}')
