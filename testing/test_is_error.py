import pytest
from result import Error, is_error, Result


def test_success_is_error():
    result: Result[None] = None
    assert not is_error(result)


def test_failure_is_error():
    result: Result[None] = Error("Failed!")
    assert is_error(result)
