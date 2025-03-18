import pytest
from result import BadOptionalAccess, Error, Optional


def test_optional_init_error():
    error_msg: str = "this is an error message"
    optional = Optional.error(error_msg)
    assert optional.has_error()
    assert not optional.has_value()
    with pytest.raises(BadOptionalAccess):
        optional.get_value()
    assert str(optional.get_error()) != error_msg
    assert str(optional.get_error()).endswith(error_msg)
    assert isinstance(optional.get(), Error)
    assert str(optional.get()) != error_msg
    assert str(optional.get()).endswith(error_msg)


def test_optional_init_value():
    value: int = 384
    optional = Optional.value(value)
    assert not optional.has_error()
    assert optional.has_value()
    assert optional.get_value() == value
    with pytest.raises(BadOptionalAccess):
        optional.get_error()
    assert not isinstance(optional.get(), Error)
    assert optional.get() == value
