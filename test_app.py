from app import greet, is_even


def test_greet():
    assert greet("Anand") == "Hello, Anand!"


def test_is_even_true():
    assert is_even(10) is True


def test_is_even_false():
    assert is_even(7) is False
