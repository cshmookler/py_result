# **Contributing Guidelines**

Ensure that your code meets the following requirements before contributing.

## Coding conventions

- The indent width is 4 for all files.
- Indent with spaces (not tabs).
    - Tabs appear strangely in different editors, but spaces are always the same.
    - Most editors are capable of automatically replacing tabs with spaces.
- All identifiers must be written in snake_case.
- Format with [black](https://github.com/psf/black).
- Lint with [mypy](https://github.com/python/mypy) and [flake8](https://github.com/PyCQA/flake8).
- Sort imports with [usort](https://github.com/facebook/usort).
- Follow [Google's style guide](https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings) for documenting functions and classes.  [Here](https://www.sphinx-doc.org/en/master/usage/extensions/example_google.html) is one example of the Google documentation style for Python.
- Code must be sufficiently documented and readable.

```text
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

## Testing

- Use [pytest](https://docs.pytest.org/en/stable/) for testing code.
- All testable functions, classes, and methods must have unit tests written for them.
- Unit tests for a specific group of functions or class should be in the same file.
- Prefix unit test files with "test_" and place them in the "testing" directory so that pytest can find them.
