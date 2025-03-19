import pytest
from result import BadOptionalAccess, Error, Optional


error_msg_1: str
error_msg_2: str
optional: Optional


@pytest.fixture(autouse=True)
def setup():
    global error_msg_1, error_msg_2, optional
    error_msg_1 = "this is an error message"
    optional = Optional.error(error_msg_1)
    error_msg_2 = "annother annotation"
    optional.trace(error_msg_2)


def test_optional_error_trace_bool():
    assert bool(optional) == False


def test_optional_error_trace_str():
    assert str(optional) != error_msg_1
    assert str(optional) != error_msg_2
    assert not str(optional).endswith(error_msg_1)
    assert str(optional).endswith(error_msg_2)
    assert error_msg_1 in str(optional)
    assert error_msg_2 in str(optional)


def test_optional_error_trace_has_error():
    assert optional.has_error()


def test_optional_error_trace_has_value():
    assert not optional.has_value()


def test_optional_error_trace_get_value():
    with pytest.raises(BadOptionalAccess):
        optional.get_value()


def test_optional_error_trace_get_error():
    assert str(optional.get_error()) != error_msg_1
    assert str(optional.get_error()) != error_msg_2
    assert not str(optional.get_error()).endswith(error_msg_1)
    assert str(optional.get_error()).endswith(error_msg_2)
    assert error_msg_1 in str(optional.get_error())
    assert error_msg_2 in str(optional.get_error())


def test_optional_error_trace_get():
    assert isinstance(optional.get(), Error)
    assert str(optional.get()) != error_msg_1
    assert str(optional.get()) != error_msg_2
    assert not str(optional.get()).endswith(error_msg_1)
    assert str(optional.get()).endswith(error_msg_2)
    assert error_msg_1 in str(optional.get())
    assert error_msg_2 in str(optional.get())
