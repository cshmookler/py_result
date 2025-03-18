from result import Error


def test_error_init():
    error_msg: str = "this is an error message"
    error = Error(error_msg)
    assert str(error) != error_msg
    assert str(error).endswith(error_msg)


def test_error_trace():
    error_msg_1: str = "this is an error message"
    error = Error(error_msg_1)
    error.trace()
    error_msg_2: str = "this is another trace annotation"
    error.trace(error_msg_2)
    error.trace()
    assert str(error) != error_msg_1
    assert str(error) != error_msg_2
    assert not str(error).endswith(error_msg_1)
    assert not str(error).endswith(error_msg_2)
    assert error_msg_1 in str(error)
    assert error_msg_2 in str(error)
    assert str(error).count("\n") == 4
