from source.config import LOCAL, APP_PATH, DEVICE_NAME, OS, AUTOMATION_NAME, OS_VERSION, PLATFORM_NAME

from pprint import pformat

from support.helpers.logger import log


class DriverCapabilities:
    def __init__(self, test_name: str):
        self.local = LOCAL
        self.app_path = APP_PATH
        self.device_name = DEVICE_NAME
        self.os = OS
        self.automation_name = AUTOMATION_NAME
        self.os_version = str(OS_VERSION)
        self.platform_name = PLATFORM_NAME

    def get_mobile_desired_capabilities(self) -> dict:
        desired_capabilities = self._get_local_mobile_desired_capabilities()
        log.info(f'Generated desired capabilities for driver:')
        log.info('\n' + pformat(desired_capabilities))
        return desired_capabilities

    def _get_local_mobile_desired_capabilities(self) -> dict:
        return {
                "app": self.app_path,
                "platformName": self.os.value,
                "automationName": self.automation_name,
                "platformVersion": self.os_version,
                "deviceName": self.device_name,

            }
