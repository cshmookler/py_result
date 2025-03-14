from py_template import hello_world


def test_hello_world_default_sep():
    assert hello_world.hello_world() == "Hello World!"


def test_hello_world_custom_sep():
    assert hello_world.hello_world("-*h>") == "Hello-*h>World!"
