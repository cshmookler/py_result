import pytest
from result import Error, Result


def test_result_typevar():
    result: Result[None] = None
    assert result is None
    result = Error("error")
    assert type(result) is Error
