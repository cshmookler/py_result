import pytest
from result import BadOptionalAccess, Result


result: Result


@pytest.fixture(autouse=True)
def setup():
    global result
    result = Result.success()


def test_result_success_str():
    assert str(result) == str(None)


def test_result_success_bool():
    assert bool(result) == True


def test_result_success_has_success():
    assert result.has_success() == True


def test_result_success_has_failure():
    assert result.has_failure() == False


def test_result_success_get():
    assert result.get() is None


def test_result_success_get_error():
    with pytest.raises(BadOptionalAccess):
        result.get_error()


def test_result_success_trace():
    with pytest.raises(BadOptionalAccess):
        result.trace()
