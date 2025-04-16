# **py_result**

A compromise between error codes and exceptions.  Provides result types with detailed error messages and stack traces.

This is a port of [cpp_result](https://github.com/cshmookler/cpp_result) for Python.

## Quickstart

#### 1.&nbsp; Install Python and Git.

##### Windows:

2. [Python](https://python.org/downloads/) (interpreted scripting language)
    - Select the "Add python.exe to PATH" option.
    - Before closing the setup wizard after setup, click the "Disable path length limit" button.
1. [Git](https://git-scm.com/downloads/) (distributed version control)

##### MacOS:

```zsh
brew install python git
```

##### Linux (Arch):

```bash
sudo pacman -S python git
```

#### 2.&nbsp; Clone this project and enter its root directory.

```bash
git clone https://github.com/cshmookler/py_result
cd py_result
```

#### 3.&nbsp; Install this library globally.

```bash
pip install .
```

#### 4.&nbsp; (Optional) Install [pytest](https://docs.pytest.org/en/stable/) and run all tests.

```bash
pip install pytest
pytest
```
