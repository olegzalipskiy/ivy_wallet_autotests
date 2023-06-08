import json

import allure
import curlify as curlify

from requests import Response
from selenium.common.exceptions import StaleElementReferenceException

from support.helpers.logger import log


def log_until(func):
    def wrapper(*args, **kwargs):
        if len(args) == 3:
            wait, expected_condition_func, timeout = args
            start_wait_msg = f'Start waiting {func.__name__} with {expected_condition_func} for {timeout} seconds'
            finish_wait_msg = f'Finish waiting for {func.__name__} with {expected_condition_func}'
        elif len(args) == 4:
            wait, expected_condition_func, timeout, text = args
            start_wait_msg = f'Start waiting {func.__name__} with {expected_condition_func} ' \
                             f'for text [{text}] for {timeout} seconds'
            finish_wait_msg = f'Finish waiting for {func.__name__} with {expected_condition_func}'
        else:
            raise ValueError(f'Unexpected arguments quantity: {len(args)}. Got arguments: {args}')

        log.debug(start_wait_msg)
        func_result = func(*args, **kwargs)
        log.debug(finish_wait_msg)
        return func_result
    return wrapper


def handle_stale_element_exception(func):
    def wrapper(*args, **kwargs):
        try:
            func_result = func(*args, **kwargs)
        except StaleElementReferenceException as sere:
            log.debug(f'StaleElementReferenceException handling. {sere}')
            func_result = handle_stale_element_exception(func)
        return func_result
    return wrapper


def log_http_request(func):
    def wrapper(*args, **kwargs):
        http_method, uri, request_separator = func.__name__.upper(), args[1], '-' * 120
        with allure.step(f'Sending [{http_method}] request to [{uri}] uri'):
            log.info(f'{request_separator}\nSending [{http_method}] request to [{uri}] url with params:\n{str(kwargs)}')
            response: Response = func(*args, **kwargs)

            response_code_text = f'{response.status_code}'
            try:
                response_body_text = f'{json.dumps(response.json(), indent=4)}'
            except json.JSONDecodeError:
                response_body_text = f'RESPONSE BODY: \n{response.content}'
            response_msg = f'RESPONSE CODE: {response_code_text}\nRESPONSE BODY: \n{response_body_text}'

            log.info(f'Response status code: {response.status_code}')
            log.debug(f'Response headers: {response.headers}')
            log.debug(f'Response content: {response.content}\n{request_separator}')

            allure.attach(response_msg, f'Response', allure.attachment_type.TEXT)
            allure.attach(curlify.to_curl(response.request), 'Request CURL', allure.attachment_type.TEXT)
        return response
    return wrapper
