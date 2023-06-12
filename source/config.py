import os

from support.helpers.logger import log
from support.utils.constants.mobile_os import MobileOs
from support.utils.file_system import FileSystem
from dotenv import load_dotenv

dotenv_path = FileSystem.get_absolute_path('resourcers', '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

''' ENVIRONMENT '''
LOCAL: bool = True if os.environ.get('LOCAL', default='True').upper() == 'TRUE' else False

ENVIRONMENT_URL = os.getenv('ENVIRONMENT_URL')
AUTOMATION_NAME = os.getenv('AUTOMATION_NAME')

APP_ACTIVITY = os.getenv('APP_ACTIVITY')
APP_PACKAGE = os.getenv('APP_PACKAGE')

APP_PATH = os.getenv('APP')
OS: MobileOs = MobileOs.get_platform_from_str(os.getenv('OS_NAME'))
OS_VERSION = float(os.getenv('PLATFORM_VERSION'))
DEVICE_NAME = os.getenv('DEVICE_NAME')
PLATFORM_NAME = os.getenv("PLATFORM_NAME").lower()

'''LOG INIT TESTS VARIABLES'''
log.info('Test session started with configuration:')
log.info(f'LOCAL: {LOCAL}')
log.info(f'PLATFORM NAME: {OS.value}')
log.info(f'OS VERSION: {OS_VERSION}')
log.info(f'ENVIRONMENT URL: {ENVIRONMENT_URL}')

'''URL's'''
BASE_URL = os.getenv("BASE_URL")
