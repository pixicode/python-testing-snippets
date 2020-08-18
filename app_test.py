import app
import pytest

def test_when_double_then_success():
    assert app.double(2) == 4
    

def test_when_get_initials_then_success():
    full_name = "John Doe"
    expected_initials = "JD"

    initals = app.get_initials(full_name)
    assert initals == expected_initials


def test_given_invalid_input_when_get_initials_then_throws():
    invalid_name = "Monkey D. Luffy"
    with pytest.raises(Exception):
        app.get_initials(invalid_name)


def test_when_get_many_initials_then_success():

    name_and_expected_initials = [
        ("John Doe", "JD"),
        ("Kate Lee", "KL"),
        ("Luke Skywalker", "LS")
    ]

    for name, expected_initials in name_and_expected_initials:
        initals = app.get_initials(name)
        assert initals == expected_initials