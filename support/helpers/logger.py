import os

from datetime import datetime

from loguru import logger as log

from support.utils.file_system import FileSystem

DATE_FORMAT = "%d-%m-%Y_%H-%M_%S"

log_folder_path = FileSystem.get_absolute_path('logs')
log_name = f"log_{datetime.now().strftime(DATE_FORMAT)}.log"
file_name = os.path.join(log_folder_path, log_name)
if not os.path.exists(log_folder_path):
    os.makedirs(log_folder_path)

log.add(file_name)