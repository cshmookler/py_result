import pytest
from result import Error


error_1: Error
error_msg: str
error_2: Error
exception_msg: str
error_3: Error


@pytest.fixture(autouse=True)
def setup():
    global error_1, error_msg, error_2, exception_msg, error_3

    error_1 = Error()
    error_msg = "this is an error message"

    error_2 = Error(error_msg)

    exception_msg = "this is an exception error message"
    try:
        raise Exception(exception_msg)
    except BaseException as exception:
        error_3 = Error(exception)


def test_error_str():
    global error_1, error_msg, error_2, exception_msg, error_3

    assert len(str(error_1)) > 0

    assert str(error_2) != error_msg
    assert str(error_2).endswith(error_msg)

    assert str(error_3) != exception_msg
    assert str(error_3).endswith(exception_msg)
