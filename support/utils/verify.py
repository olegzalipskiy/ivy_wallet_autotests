from typing import Any, Collection

from support.helpers.logger import log


class Verify:

    @staticmethod
    def equal(actual_result: Any, expected_result: Any, verify_message: str) -> None:
        type_err_msg = f'Expect to compare same types. Got {type(actual_result)}, {type(expected_result)}'
        assert type(actual_result) == type(expected_result), type_err_msg
        try:
            assert actual_result == expected_result, verify_message
        except AssertionError as ae:
            log.critical(f"AssertionError: {ae.args[0]}")
            raise ae

    @staticmethod
    def collection_is_empty(collection: Collection, verify_message: str) -> None:
        try:
            assert len(collection) == 0, verify_message
        except AssertionError as ae:
            log.critical(f"AssertionError: {ae.args[0]}")
            raise ae

    @staticmethod
    def is_true(actual_result: bool, verify_message: str) -> None:
        try:
            assert actual_result, verify_message
        except AssertionError as ae:
            log.critical(f"AssertionError: {ae.args[0]}")
            raise ae

    @staticmethod
    def is_false(actual_result: bool, verify_message: str) -> None:
        try:
            assert not actual_result, verify_message
        except AssertionError as ae:
            log.critical(f"AssertionError: {ae.args[0]}")
            raise ae
