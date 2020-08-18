# Python Testing Snippets

This is a small project with examples for basic unit testing, test setup/tear-down, and mocking. I intended these snippets to be minimal yet useful for fundamental Python testing.

## Requirements

The only requirement for this package is [pytest](https://docs.pytest.org/en/stable/). These scripts were written and tested in Python `3.7` with pytest version `5.4.3`.

```bash
pip install pytest
```

## Usage

#### Running all tests in the project

```bash
pytest
```

If this command is executed in the project directory (the same directory as this README), it will 'discover' all tests in the project and run them.

Pytest [discovers tests](https://docs.pytest.org/en/stable/goodpractices.html#test-discovery) in this directory primarily by naming convention.

> In those directories, search for `test_*.py` or `*_test.py` files, imported by their [test package name](https://docs.pytest.org/en/stable/goodpractices.html#test-package-name).
>
> From those files, collect test items:
>
> - `test` prefixed test functions or methods outside of class
> - `test` prefixed test functions or methods inside `Test` prefixed test classes (without an `__init__` method)

#### Running a specific tests

```bash
# Run all tests in a file.
pytest app_test.py

# Run a specific test function
pytest app_test.py::test_when_double_then_success
```

The second command will run the test function called `test_when_double_then_success()` in the file `app_test.py`.

#### Run tests and show `print()` output

For tests that pass, `print` output is not re-directed to the terminal by default. If you're missing some output, try adding this argument:

```
pytest -s
```

## Snippets

#### Basic test

```python
def test_something():
    # If true, this will pass.
    assert True
```

#### Expect a test to raise an Exception

```python
def test_something_2():
    with pytest.raises(SomeException):
    	# If this doesn't raise 'SomeException', the test will fail.
        app.do_something_invalid()
```

#### Mock functions or classes

```python
from unittest.mock import Mock

# Create a mock object called 'mock_webscraper'.
mock_webscraper = Mock()

# Create a mock object, called 'scrape' as a property of mock_webscraper.
# If we call mock_webscraper.scrape(), it will return 'hello world!'
mock_webscraper.scrape = Mock(return_value="hello world!")
```

#### Test setup and tear down

```python
def setup_module():
    print("Do something at the start of this test module.")

def teardown_module():
    print("Do something before this test module exits.")
```

## References

* [GIVEN-WHEN-THEN Testing Style](https://martinfowler.com/bliki/GivenWhenThen.html)
* [Pytest Documentation](https://docs.pytest.org/en/stable/)
* [Python Unittest Documentation](https://docs.python.org/3/library/unittest.html)