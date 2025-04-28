import pytest
from result import BadErrorConstruction, Error, Optional, Result


def test_result_error_init_none():
    with pytest.raises(BadErrorConstruction):
        Result.failure(None)


def test_result_error_init_str():
    error_msg: str = "this is an example error"
    result = Result.failure(error_msg)
    assert result.has_failure()
    assert str(result.get_error()).endswith(error_msg)


def test_result_error_init_error():
    error_msg: str = "this is an example error"
    result = Result.failure(Error(error_msg))
    assert result.has_failure()
    assert str(result.get_error()).endswith(error_msg)


def test_result_error_init_result():
    error_msg: str = "this is an example error"
    result = Result.failure(Result.failure(error_msg))
    assert result.has_failure()
    assert str(result.get_error()).endswith(error_msg)


def test_result_error_init_optional():
    error_msg: str = "this is an example error"
    result = Result.failure(Optional.error(error_msg))
    assert result.has_failure()
    assert str(result.get_error()).endswith(error_msg)
