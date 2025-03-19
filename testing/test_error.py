import pytest
from result import Error


error_msg: str
error: Error


@pytest.fixture(autouse=True)
def setup():
    global error_msg, error
    error_msg = "this is an error message"
    error = Error(error_msg)


def test_error_str():
    assert str(error) != error_msg
    assert str(error).endswith(error_msg)
