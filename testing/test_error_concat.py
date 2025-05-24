from result import Error


def test_error_concat():
    error_msg_1 = "first error"
    error_1 = Error(error_msg_1)

    error_msg_2 = "second error"
    error_2 = Error(error_msg_2)

    concat_error = error_1.concat(error_2)

    assert error_msg_1 in str(concat_error)
    assert error_msg_2 in str(concat_error)
