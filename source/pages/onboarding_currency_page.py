from appium.webdriver.common.mobileby import MobileBy

from source.pages.base_page import BasePage
from support.helpers.mobile_locator import MobileLocator


class OnboardingCurrencyPage(BasePage):
    _TITLE = MobileLocator(
        android=(MobileBy.XPATH,
                 '//android.widget.TextView[@text="Choose currency"]')
    )

    _SUGGESTED_TITLE = MobileLocator(
        android=(MobileBy.XPATH,
                 '//android.widget.TextView[@text=Suggested]')
    )

    _CROSS_BUTTON = MobileLocator(
        android=(MobileBy.XPATH,
                 '(//android.widget.ImageView[@content-desc="icon button"])[1]')
    )

    _SEARCH_BUTTON = MobileLocator(
        android=(MobileBy.XPATH,
                 '(//android.widget.ImageView[@content-desc="icon button"])[2]')
    )

    _CHOOSE_BUTTON = MobileLocator(
        android=(MobileBy.XPATH,
                 '//android.view.View[@content-desc="icon"]/ancestor::android.view.View[4]')
    )

    _SEARCH_FIELD = MobileLocator(
        android=(MobileBy.XPATH,
                 '//android.widget.TextView[@text="Search (e.g. EUR, USD, BTC)"]/ancestor::android.widget.EditText')
    )

    _SEARCH_PLACEHOLDER = MobileLocator(
        android=(MobileBy.XPATH,
                 '//android.widget.TextView[@text="Search (e.g. EUR, USD, BTC)"]')
    )

    _SEARCH_ICON = MobileLocator(
        android=(MobileBy.XPATH,
                 '(//android.view.View[@content-desc="icon"])[1]')
    )

    _CANCEL_SEARCH_BUTTON = _SEARCH_BUTTON


class SelectedCurrencyElement(BasePage):

    @staticmethod
    def generate_selected_currency_locator(currency: str) -> MobileLocator:
        return MobileLocator(
            android=(MobileBy.XPATH,
                     f'//android.widget.TextView[@text="Selected"]/preceding-sibling::android.widget.TextView[@text="{currency}"]')
        )