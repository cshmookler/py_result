import pytest
from result import BadOptionalAccess, Result


error_msg: str
result: Result


@pytest.fixture(autouse=True)
def setup():
    global error_msg, result
    error_msg = "this is an error message"
    result = Result.failure(error_msg)


def test_result_failure_str():
    assert str(result) != error_msg
    assert str(result).endswith(error_msg)
    assert error_msg in str(result)


def test_result_failure_bool():
    assert bool(result) == False


def test_result_failure_has_success():
    assert result.has_success() == False


def test_result_failure_has_failure():
    assert result.has_failure() == True


def test_result_failure_get():
    assert str(result.get()) != error_msg
    assert str(result.get()).endswith(error_msg)
    assert error_msg in str(result.get())


def test_result_failure_get_error():
    assert str(result.get_error()) != error_msg
    assert str(result.get_error()).endswith(error_msg)
    assert error_msg in str(result.get_error())
