import pytest
from result import BadOptionalAccess, Error, Optional


error_msg: str
optional: Optional


@pytest.fixture(autouse=True)
def setup():
    global error_msg, optional
    error_msg = "this is an error message"
    optional = Optional.error(error_msg)


def test_optional_error_bool():
    assert bool(optional) == False


def test_optional_error_str():
    assert str(optional) != error_msg
    assert str(optional).endswith(error_msg)


def test_optional_error_has_error():
    assert optional.has_error()


def test_optional_error_has_value():
    assert not optional.has_value()


def test_optional_error_get_value():
    with pytest.raises(BadOptionalAccess):
        optional.get_value()


def test_optional_error_get_error():
    assert str(optional.get_error()) != error_msg
    assert str(optional.get_error()).endswith(error_msg)


def test_optional_error_get():
    assert isinstance(optional.get(), Error)
    assert str(optional.get()) != error_msg
    assert str(optional.get()).endswith(error_msg)


def test_optional_value_trace():
    value: int = 384
    optional = Optional.value(value)
    error_msg: str = "an annotation"
    with pytest.raises(BadOptionalAccess):
        optional.trace(error_msg)
