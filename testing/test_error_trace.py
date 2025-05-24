import pytest
from result import Error


error_msg_1: str
error_msg_2: str
error: Error


@pytest.fixture(autouse=True)
def setup():
    global error_msg_1, error_msg_2, error

    error_msg_1 = "this is an error message"
    error = Error(error_msg_1)

    assert error.trace() is error
    error_msg_2 = "this is another trace annotation"
    assert error.trace(error_msg_2) is error


def test_error_trace_str():
    global error_msg_1, error_msg_2, error

    assert str(error) != error_msg_1
    assert str(error) != error_msg_2
    assert not str(error).endswith(error_msg_1)
    assert str(error).endswith(error_msg_2)
    assert error_msg_1 in str(error)
    assert error_msg_2 in str(error)
    assert str(error).count("\n") == 3
