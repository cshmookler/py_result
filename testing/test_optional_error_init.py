import pytest
from result import BadErrorConstruction, Error, Optional, Result


def test_optional_error_init_none():
    with pytest.raises(BadErrorConstruction):
        Optional.error(None)


def test_optional_error_init_str():
    error_msg: str = "this is an example error"
    optional = Optional.error(error_msg)
    assert optional.has_error()
    assert str(optional.get_error()).endswith(error_msg)


def test_optional_error_init_error():
    error_msg: str = "this is an example error"
    optional = Optional.error(Error(error_msg))
    assert optional.has_error()
    assert str(optional.get_error()).endswith(error_msg)


def test_optional_error_init_result():
    error_msg: str = "this is an example error"
    optional = Optional.error(Result.failure(error_msg))
    assert optional.has_error()
    assert str(optional.get_error()).endswith(error_msg)


def test_optional_error_init_optional():
    error_msg: str = "this is an example error"
    optional = Optional.error(Optional.error(error_msg))
    assert optional.has_error()
    assert str(optional.get_error()).endswith(error_msg)
