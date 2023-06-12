import logging

import allure
import pytest

from loguru import logger

from support.helpers.drivers.driver_capabilities import DriverCapabilities
from support.helpers.drivers.mobile_driver import MobileDriverWrapper
from support.helpers.logger import log
from support.helpers.page_object_factory import POF


@pytest.fixture(autouse=True)
def mobile_driver(request):
    test_name = request.node.name
    log.info(f'Start initializing mobile driver for test: {request.node.name}')
    dc = DriverCapabilities(test_name)
    desired_capabilities = dc.get_mobile_desired_capabilities()
    mobile_driver = MobileDriverWrapper(desired_capabilities)

    setattr(request.cls, "mobile_driver", mobile_driver)
    POF.mobile_driver = mobile_driver

    yield request.cls.mobile_driver
    mobile_driver.close_driver()


@pytest.fixture(autouse=True)
def caplog(caplog):
    class PropogateHandler(logging.Handler):
        def emit(self, record):
            logging.getLogger(record.name).handle(record)

    handler_id = logger.add(PropogateHandler(), format="{message}")
    yield caplog
    logger.remove(handler_id)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    try:

        if rep.when == 'call' and rep.failed:
            drivers = {}
            if 'mobile_driver' in item.fixturenames:
                drivers['mobile_driver'] = item.funcargs['mobile_driver'].driver
            if 'web_driver' in item.fixturenames:
                drivers['web_driver'] = item.funcargs['web_driver'].driver
            if not drivers:
                log.critical('Failed to take screen-shot. No existing driver')
            else:
                for driver in drivers:
                    allure.attach(
                        drivers[driver].get_screenshot_as_png(),
                        name=f'{driver} screenshot',
                        attachment_type=allure.attachment_type.PNG
                    )
                    allure.attach(
                        drivers[driver].page_source,
                        name=f'{driver} page source',
                        attachment_type=allure.attachment_type.TEXT
                    )

    except Exception as e:
        log.critical(f'Fail to take screen-shot or page source: {e}')
