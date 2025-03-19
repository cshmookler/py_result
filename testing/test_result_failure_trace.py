import pytest
from result import BadOptionalAccess, Result


error_msg_1: str
error_msg_2: str
result: Result


@pytest.fixture(autouse=True)
def setup():
    global error_msg_1, error_msg_2, result
    error_msg_1 = "this is an error message"
    result = Result.failure(error_msg_1)
    result.trace()
    error_msg_2 = "another error message"
    result.trace(error_msg_2)


def test_result_failure_trace_str():
    assert str(result) != error_msg_1
    assert str(result) != error_msg_2
    assert not str(result).endswith(error_msg_1)
    assert str(result).endswith(error_msg_2)
    assert error_msg_1 in str(result)
    assert error_msg_2 in str(result)


def test_result_failure_trace_bool():
    assert bool(result) == False


def test_result_failure_trace_has_success():
    assert result.has_success() == False


def test_result_failure_trace_has_failure():
    assert result.has_failure() == True


def test_result_failure_trace_get():
    assert str(result.get()) != error_msg_1
    assert str(result.get()) != error_msg_2
    assert not str(result.get()).endswith(error_msg_1)
    assert str(result.get()).endswith(error_msg_2)
    assert error_msg_1 in str(result.get())
    assert error_msg_2 in str(result.get())


def test_result_failure_trace_get_error():
    assert str(result.get_error()) != error_msg_1
    assert str(result.get_error()) != error_msg_2
    assert not str(result.get_error()).endswith(error_msg_1)
    assert str(result.get_error()).endswith(error_msg_2)
    assert error_msg_1 in str(result.get_error())
    assert error_msg_2 in str(result.get_error())
