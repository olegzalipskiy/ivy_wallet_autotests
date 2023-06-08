from source.config import LOCAL, APP_ACTIVITY, BROWSERSTACK_USER, BROWSERSTACK_KEY, DEVICE_NAME, OS_VERSION, \
    PROJECT_NAME, BUILD_NAME, TEST_NAME, APP_PATH, OS, AUTOMATION_NAME, LANGUAGE, PLATFORM_NAME, REAL_DEVICE, \
    XCODEORGID, XCODESIGNINID, UDID, BUNDLEID, BROWSERSTACK_LOCAL

from pprint import pformat

from support.helpers.logger import log


class DriverCapabilities:
    def __init__(self, test_name: str):
        self.local = LOCAL
        self.app_activity = APP_ACTIVITY
        self.bs_user = BROWSERSTACK_USER
        self.bs_key = BROWSERSTACK_KEY
        self.app_path = APP_PATH
        self.device_name = DEVICE_NAME
        self.os = OS
        self.os_version = str(OS_VERSION)
        self.project_name = PROJECT_NAME
        self.build_name = BUILD_NAME
        self.test_name = TEST_NAME if TEST_NAME else test_name
        self.automation_name = AUTOMATION_NAME
        self.language = LANGUAGE if LANGUAGE else 'en'
        self.platform_name = PLATFORM_NAME
        self.real_device = REAL_DEVICE
        self.xcodeorgid = XCODEORGID
        self.xcodesigninid = XCODESIGNINID
        self.udid = UDID
        self.bundle_id = BUNDLEID
        self.bs_local = BROWSERSTACK_LOCAL

    def get_mobile_desired_capabilities(self) -> dict:
        if self.local and self.real_device:
            desired_capabilities = self._get_real_device_desire_capabilities()
        elif self.local and not self.real_device:
            desired_capabilities = self._get_local_mobile_desired_capabilities()
        log.info(f'Generated desired capabilities for driver:')
        log.info('\n' + pformat(desired_capabilities))
        return desired_capabilities

    def _get_local_mobile_desired_capabilities(self) -> dict:
        if self.language == 'es':
            return {
                "appActivity": self.app_activity,
                "app": self.app_path,
                "platformName": self.os.value,
                "automationName": self.automation_name,
                "platformVersion": self.os_version,
                "deviceName": self.device_name,
                "language": "es",
                "locale": "ES",
            }
        else:
            return {
                "appActivity": self.app_activity,
                "app": self.app_path,
                "platformName": self.os.value,
                "automationName": self.automation_name,
                "platformVersion": self.os_version,
                "deviceName": self.device_name,
                "language": "en",
                "locale": "GB",
            }

    def _generate_language_capabilities(self):
        if self.os.value == "iOS":
            return {
                "locale": self.language.lower() + "_" + self.language.upper(),
                "language": self.language.lower()
            }

        elif self.os.value == "Android":
            locale = "ES" if self.language == "es" else "GB"
            return {
                "locale": locale,
                "language": self.language.lower()
            }

    def _get_real_device_desire_capabilities(self) -> dict:
        language_capabilities = self._generate_language_capabilities()
        base_capabilities = {
            "platformName": self.os.value,
            "platformVersion": self.os_version,
            "automationName": self.automation_name,
            "deviceName": self.device_name,
            "app": self.app_path
        }

        if self.os.value == "iOS":
            additional_platform_capabilities = {
                "bundleId": self.bundle_id,
                "xcodeOrgid": self.xcodeorgid,
                "xcodesigninId": self.xcodesigninid,
                "udid": self.udid
            }

        elif self.os.value == "Android":
            additional_platform_capabilities = {
                "noSign": True
            }

        else:
            additional_platform_capabilities = {}

        return base_capabilities | language_capabilities | additional_platform_capabilities
