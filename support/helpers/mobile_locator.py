from typing import Union

from support.helpers.logger import log

from source.config import OS
from support.utils.constants.mobile_os import MobileOs


class MobileLocator:
    def __init__(self, android: tuple = None, ios: tuple = None,
                 android_attribute: str = None, ios_attribute: str = None):
        self.os = OS
        self.data = {
            MobileOs.ANDROID: {
                'locator': android,
                'attribute': android_attribute
            },
            MobileOs.IOS: {
                'locator': ios,
                'attribute': ios_attribute
            }
        }

        if self.data[MobileOs.IOS]['locator'] is None and self.data[MobileOs.ANDROID]['locator'] is None:
            log.critical('No locators were found')
            raise AttributeError('No locators were found')

    def __call__(self, attribute: str = None) -> Union[tuple[str, str], str]:
        if not attribute:
            if not self.data[self.os]['locator']:
                raise AttributeError(f'Locator is not valid. Locator value: {self.data[self.os]["locator"]}')
            else:
                return self.data[self.os]['locator']
        elif attribute == 'attribute':
            return self.data[self.os]['attribute']