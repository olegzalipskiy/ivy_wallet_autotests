from enum import Enum
from typing import Union


class MobileOs(Enum):
    ANDROID = 'Android'
    IOS = 'iOS'

    @classmethod
    def get_platform_from_str(cls, mobile_os_string: str) -> Union[str, 'MobileOs']:
        if mobile_os_string is None:
            return "OS not Defined"
        else:
            for _ in MobileOs:
                if _.value.lower() == mobile_os_string.lower():
                    return _
        raise ValueError(f'Can not transform string [{mobile_os_string}] to existing OS')
