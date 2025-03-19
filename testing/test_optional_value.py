import pytest
from result import BadOptionalAccess, Error, Optional


value: int
optional: Optional


@pytest.fixture(autouse=True)
def setup() -> None:
    global value, optional
    value = 384
    optional = Optional.value(value)


def test_optional_value_bool():
    assert bool(optional) == True


def test_optional_value_str():
    assert str(optional) == str(value)


def test_optional_value_has_error():
    assert not optional.has_error()


def test_optional_value_has_value():
    assert optional.has_value()


def test_optional_value_get_value():
    assert optional.get_value() == value


def test_optional_value_get_error():
    with pytest.raises(BadOptionalAccess):
        optional.get_error()


def test_optional_value_get():
    assert not isinstance(optional.get(), Error)
    assert optional.get() == value


def test_optional_value_trace():
    with pytest.raises(BadOptionalAccess):
        optional.trace()
    error_msg: str = "an annotation"
    with pytest.raises(BadOptionalAccess):
        optional.trace(error_msg)
